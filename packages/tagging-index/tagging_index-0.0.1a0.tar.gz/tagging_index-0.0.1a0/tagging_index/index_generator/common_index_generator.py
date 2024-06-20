from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from os import path
from pathlib import Path
from typing import Dict, List, TypeVar
import pandas as pd
from tagging_index.maxcompute import SqlRunner


sql_create_table = """
    CREATE TABLE IF NOT EXISTS dwd_digital_index(
	comp_id STRING,
    company_abbr string,
    index_name string,
	index_value string,
    eff_year STRING
    ) 
    PARTITIONED  by  (
    index_version string,
    comp_type string,
    index_code string
    );
    """


@dataclass(frozen=True)
class IndexSqlTemplate:
    sql_comp_map: str
    sql_source_tag_data: str
    sql_year_sequence: str
    index_version: str
    comp_type: str
    index_code: str
    index_name: str
    dwd_table: str
    # TODO add year range constraint for source data
    INDEX_TEMPLATE_SELECT = """ 
        SELECT /*+ MAPJOIN(y) */
            a.comp_id
            ,a.company_abbr
            ,"{index_name}" as index_name
            ,count(DISTINCT entity_id) as index_value
            ,y.eff_year
            ,CONCAT_ws('-','{index_version}',b.tag_udf_version) as index_version 
            ,"{comp_type}" as comp_type
            ,"{index_code}" as index_code
        FROM
        {sql_comp_map} a join {sql_source_tag_data} b on a.source_comp_id = b.source_comp_id
        join {sql_year_sequence} y 
        on b.end_year>=y.eff_year and b.start_year<=y.eff_year  
        group by a.comp_id,a.company_abbr,y.eff_year,b.tag_udf_version
        ;
        """
    INDEX_TEMPLATE_INSERT = (
        "INSERT OVERWRITE TABLE {dwd_table} PARTITION (index_version,comp_type,index_code) "
        + INDEX_TEMPLATE_SELECT
    )


class CommonIndexGenerator(ABC):
    # define the sql template as static property
    DWD_TABLE = "dwd_digital_index"
    _sql_comp_map_lst_com = """ ( 
                SELECT distinct full_stock_id as comp_id
                ,full_stock_id source_comp_id
                ,nvl(abbr_cn,company_name_cn) company_abbr
                FROM dim_china_listed_company 
                WHERE pt = MAX_PT('dim_china_listed_company')
            )
        """

    @property
    def sql_comp_map_lst_com(self):
        return self._sql_comp_map_lst_com

    @property
    def sql_comp_map(self):
        if self.comp_type == "lst_com":
            cte_comp_map = self.sql_comp_map_lst_com
        else:
            raise ValueError(f"not implemented for comp_type: {self.comp_type}")
        return cte_comp_map

    @property
    @abstractmethod
    def _sql_src_ttl_lst_com(self) -> str:
        pass

    @property
    @abstractmethod
    def _table_source_tag_lst_com(self) -> str:
        pass

    @abstractmethod
    def get_sql_source_tag_lst_com(
        self, tag_condition: str, tag_udf_version: str
    ) -> str:
        pass

    _sql_year_sequence = """ 
            (SELECT EXPLODE(SEQUENCE({start_year},{end_year})) as (eff_year))
    """

    @property
    def sql_year_sequence(self):
        sql_year_sequence = self._sql_year_sequence.format(
            **{"start_year": self.start_year, "end_year": self.end_year}
        )
        return sql_year_sequence

    @classmethod
    @abstractmethod
    def get_source_name(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_index_suffix(cls) -> str:
        pass

    def __init__(self, tag_desc_file: str):
        self._tag_desc_file = tag_desc_file
        self.tag_udf_version = ""
        self.start_year = 2000
        self.end_year = 2024
        self.comp_type = "lst_com"
        meta_json = json.load(open(self._tag_desc_file))
        self.version = meta_json["version"]
        self.tag_version = meta_json["tag_version"]
        self.index_meta = {
            index_definition["index_code"]: index_definition
            for index_definition in meta_json["index_definition"]
        }
        self.global_exclude = meta_json.get("exclude", {})
        # self.df_index_meta=pd.DataFrame(self.index_meta)

    @property
    def index_codes(self) -> List[str]:
        return [
            f"{index_code}_{self.get_index_suffix()}"
            for index_code in list(self.index_meta.keys())
        ]

    def generate_sql(self, index_codes: List[str] = []) -> Dict[str, str]:
        return self._generate_sql(index_codes)

    def __get_source_version_cond(self, source_ver: str) -> str:
        src_data_ver_cond = (
            f'"{source_ver}"'
            if source_ver
            else f'max_pt("{self._table_source_tag_lst_com}")'
        )
        return src_data_ver_cond

    def _generate_sql(
        self, index_codes: List[str] = [], return_result=False
    ) -> Dict[str, str]:
        index_generator_sql = {}
        if index_codes is None or len(index_codes) == 0:
            index_codes = list(self.index_meta.keys())

        for index_code in index_codes:
            template = self.get_index_sql_template(index_code)
            sql_template = (
                template.INDEX_TEMPLATE_SELECT
                if return_result
                else template.INDEX_TEMPLATE_INSERT
            )
            index_generator_sql[index_code] = sql_template.format(**template.__dict__)

        return index_generator_sql

    def get_index_sql_template(self, index_code: str) -> IndexSqlTemplate:
        src_data_ver_cond = self.__get_source_version_cond(self.tag_udf_version)
        tag_condition = self._generate_tag_condition(
            self.index_meta[index_code]["condition"], self.tag_version
        )
        if self.comp_type == "lst_com":
            sql_source_tag_data = self.get_sql_source_tag_lst_com(
                tag_condition, src_data_ver_cond
            )
        else:
            raise ValueError(f"not implemented for comp_type: {self.comp_type}")
        index_sql_template = IndexSqlTemplate(
            sql_comp_map=self.sql_comp_map,
            sql_source_tag_data=sql_source_tag_data,
            sql_year_sequence=self.sql_year_sequence,
            index_version=self.version,
            comp_type=self.comp_type,
            index_code=f"{index_code}_{self.get_index_suffix()}",
            index_name=self.index_meta[index_code]["index_name"],
            dwd_table=self.DWD_TABLE,
        )
        return index_sql_template

    def generate_index(self, index_codes: List[str] = []):
        index_sql = self.generate_sql(index_codes)
        print(
            f"*****{self.get_source_name()} index generater config: [comp:{self.comp_type},tag:{self.tag_version},source:{self.tag_udf_version or 'latest source version'}] ..."
        )
        for index_code, sql in index_sql.items():
            index_name = self.index_meta[index_code]["index_name"]
            print(f"generating index: {index_name}[code:{index_code}] ...")
            result = self._run(sql)
            print(
                f"done: {index_name}[{index_code}](total records:{result[0].outputs[0].rows})"
            )

    def generate_index_ttl(self):
        index_sql = self.generate_total_sql()
        print(
            f"generating total count index: [{self.get_source_name()},{self.comp_type}] ..."
        )
        result = self._run(index_sql)
        print(f"done: total count index (total records:{result[0].outputs[0].rows})")

    def generate_total_sql(self):
        index_config = IndexSqlTemplate(
            sql_comp_map=self.sql_comp_map,
            sql_source_tag_data=self._sql_src_ttl_lst_com,
            sql_year_sequence=self.sql_year_sequence,
            index_version=self.get_source_name(),
            comp_type=self.comp_type,
            index_code="ttl_cnt",
            index_name="total count of source",
            dwd_table=self.DWD_TABLE,
        )
        sql = index_config.INDEX_TEMPLATE_INSERT.format(**index_config.__dict__)
        return sql

    def _generate_tag_condition(self, condition: dict, tag_version):
        category_sql_parts = []
        dim_table = "dim_digitalization_tag"
        dim_view = "v_dim_digital_tag_level"
        or_cond = condition.get("or", {})
        exclude = condition.get("exclude", {}) or self.global_exclude
        tag_version_cond = (
            f'"{tag_version}"' if tag_version else f'max_pt("{dim_table}")'
        )
        exclude_tag_cond = (
            " tag not in ("
            + ",".join([f"'{tag}'" for tag in exclude.get("tags")])
            + ")"
            if exclude.get("tags", [])
            else "1=1"
        )
        for level, tags in or_cond.items():
            tags_str = ", ".join([f"'{tag}'" for tag in tags])
            category_sql_parts.append(f"tag_lv{level[-1]} in ({tags_str})")
        if not category_sql_parts:
            category_sql_parts = ["1=1"]
        category_sql_query = f""" tag in (SELECT tag FROM {dim_view} 
            WHERE tag_version={tag_version_cond}
            AND ( {' OR '.join(category_sql_parts)})
            and {exclude_tag_cond}
            )
        """
        return category_sql_query

    def get_index_data(self, index_code: str) -> pd.DataFrame:
        """return specified index data in dataframe rather than insert into table

        Args:
            index_code (str)

        Returns:
            pd.DataFrame:
        """
        sql = self._generate_sql([index_code], return_result=True).get(index_code)
        if sql:
            df = SqlRunner(sql).to_pandas()
            return df
        else:
            raise ValueError(f"index code {index_code} not found")

    def _run(self, sql):
        sql_runner = SqlRunner(sql)
        sql_runner.run()
        summary = sql_runner.get_summary()
        # print(summary[0].outputs_partitions)
        return summary

    @staticmethod
    def get_index_schema():
        schema_file = Path(__file__).parent / "index_tag_schema.json"
        return json.load(open(schema_file, encoding="utf-8", mode="r"))


TIndexGenerator = TypeVar("TIndexGenerator", bound=CommonIndexGenerator)
