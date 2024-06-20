from typing import Dict, List, Type
from dataclasses import dataclass
from tagging_index.index_generator import TIndexGenerator
from data2cloud.cloud.maxcompute import SqlRunner


class DashboardAdsGenerator:
    @dataclass
    class AdsColumns:
        comp_id: str = "comp_id"
        company_abbr: str = "company_abbr"
        industry_name: str = "industry_name"
        eff_year: str = "eff_year"
        index_version: str = "index_version"
        ttl_cnt: str = "ttl_cnt"
        it_cnt: str = "it_cnt"
        source_name: str = "source_type"
        index_name: str = "index_type"
        index_value: str = "index_value_cnt"

    def __init__(self, source_cls: List[Type[TIndexGenerator]]):
        self.source_cls = source_cls
        self.comp_type = "lst_com"
        self.index_version = ""
        self._it_total_code = "IT_total"
        self.index_codes = []
        self.ads_columns = self.AdsColumns()

        self.start_year = 2000
        self.end_year = 2024
        self.comp_list = []

    def _generate_ttl_sql(self) -> Dict[str, str]:
        ttl_sql = {}
        comp_list = (
            ",".join([f'"{x}"' for x in self.comp_list]) if self.comp_list else ""
        )
        comp_cond = (
            f"comp_id in ({comp_list})" if self.comp_list else "comp_id is not null"
        )
        for c in self.source_cls:
            ttl_sql[c.get_source_name()] = (
                f"""  (
                select comp_id,index_value,eff_year 
                from {c.DWD_TABLE} where index_version = "{c.get_source_name()}-total" 
                and comp_type = "{self.comp_type}"
                and index_code = "ttl_cnt"
                and eff_year >= {self.start_year} and eff_year <= {self.end_year}
                and {comp_cond}
                )
                """
            )
        return ttl_sql

    def _get_index_ver_cond(self, cls: Type[TIndexGenerator]) -> str:
        if self.index_version:
            return f"'{self.index_version}'"
        else:
            return f"(select max(index_version) from {cls.DWD_TABLE} where index_version not like '%-total')"

    # special index for IT total
    def _generate_index_it_ttl_sql(self) -> Dict[str, str]:
        index_sql = {}
        for c in self.source_cls:
            index_sql[c.get_source_name()] = (
                f"""  (
            select comp_id,index_value,eff_year 
            from {c.DWD_TABLE} where index_version = {self._get_index_ver_cond(c)}
            and comp_type = "{self.comp_type}" and index_code = '{self._it_total_code}'
            and eff_year >= {self.start_year} and eff_year <= {self.end_year}
            )
            """
            )
        return index_sql

    def _generate_index_sql(self) -> Dict[str, str]:
        index_sql = {}

        for c in self.source_cls:
            index_code_list = ",".join(
                f"'{x}_{c.get_index_suffix()}'" for x in self.index_codes
            )
            index_sql[c.get_source_name()] = (
                f""" (
                select comp_id,index_code,index_name,index_value,eff_year,index_version
                from {c.DWD_TABLE} where index_version = {self._get_index_ver_cond(c)}
                and comp_type = "{self.comp_type}"
                and index_code in ( {index_code_list} )
                and eff_year >= {self.start_year} and eff_year <= {self.end_year}
                )
                """
            )
        return index_sql

    _dim_com = """
        ( 
                SELECT full_stock_id as comp_id
                ,nvl(abbr_cn,company_name_cn) company_abbr
                ,industry_level1 as industry_name
                FROM dim_china_listed_company 
                WHERE pt = MAX_PT('dim_china_listed_company')
        )
    """

    def get_dim_index_code(self, index_data_sql: str):
        sql = f"""(select distinct index_code,index_name,index_version from {index_data_sql})"""
        return sql

    def _generate_dashboard_sql(self, test=False):
        if self.index_codes == []:
            raise Exception("Please set index_code first")
        ttl_sql = self._generate_ttl_sql()
        index_sql = self._generate_index_sql()
        index_it_ttl_sql = self._generate_index_it_ttl_sql()
        source_sql = []
        for c in self.source_cls:
            source = c.get_source_name()
            dim_index = self.get_dim_index_code(index_sql[source])
            source_sql.append(
                f"""select  
            a.comp_id as {self.ads_columns.comp_id}
            ,com.company_abbr as {self.ads_columns.company_abbr}
            ,com.industry_name as {self.ads_columns.industry_name}
            ,a.eff_year as {self.ads_columns.eff_year}
            ,a.index_version as {self.ads_columns.index_version}
            ,a.index_value as {self.ads_columns.ttl_cnt}
            ,b.index_value as {self.ads_columns.it_cnt}
            ,'{self.get_source_alias(c)}' as {self.ads_columns.source_name}
            ,a.index_name as {self.ads_columns.index_name}
            ,c.index_value as {self.ads_columns.index_value}
            from (
                select /*+ MAPJOIN(b) */  
                    comp_id,index_code,index_name,b.index_version
                    ,index_value
                    ,eff_year from {ttl_sql[source]} a 
                join {dim_index} b ) a
            join {self._dim_com} com on a.comp_id = com.comp_id
            left join {index_it_ttl_sql[source]} b on a.comp_id = b.comp_id and a.eff_year = b.eff_year
            left join {index_sql[source]} c on a.comp_id = c.comp_id and a.eff_year = c.eff_year and a.index_code = c.index_code
            """
            )
        combined_sql = " union all ".join(source_sql)
        ads_cols = ",".join(self.ads_columns.__dict__.values())
        dashboard_sql = f"""
            {'INSERT OVERWRITE TABLE ads_digital_talent_index_dashboard ' if not test else ' ' }
            select {ads_cols} from ({combined_sql});
        """
        return dashboard_sql

    def generate_dashboard_data(self):
        dashboard_sql = self._generate_dashboard_sql()
        print(
            f"start to generate dashboard data: [{self.comp_type},'{self.index_version}','{self.index_codes}'] ..."
        )
        SqlRunner(dashboard_sql).run()
        print(f"done: dashboard data")

    def get_source_alias(self, cls: Type[TIndexGenerator]):
        _source_map = {"talent": "stock"}
        return _source_map.get(cls.get_source_name(), cls.get_source_name())

    def get_result_df(self):
        dashboard_sql = self._generate_dashboard_sql(test=True)
        result = SqlRunner(dashboard_sql).to_pandas()
        return result
