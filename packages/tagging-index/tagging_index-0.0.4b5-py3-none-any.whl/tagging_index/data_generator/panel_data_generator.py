from dataclasses import dataclass, field
from math import e
from typing import Dict, List, Optional, Type
from tagging_index.index_generator.common_index_generator import (
    CommonIndexGenerator,
    TIndexGenerator,
)
from tagging_index.maxcompute.sql_runner import SqlRunner


@dataclass
class VariableMap:
    code: str
    column_name: Optional[str] = field(default=None)
    """if not provide, use code as column_name"""


@dataclass
class VariableMapOther:
    source_data: str
    """ the table or sql for source data, sql should bracket off """
    source_var_col: str
    var_col_name: Optional[str] = field(default=None)
    """if not provide, use source_var_col as var_col_name"""
    dim_comp_id: str = "comp_id"
    col_comp_id: str = "comp_id"
    col_year: Optional[str] = field(default=None)
    """ none for non-time sequence variable """


class PanelDataGenerator:

    def __init__(self):
        self.index_version = ""
        self.index_dwd_table = "dwd_digital_index"
        self.matrix_dwd_table = "dwd_cn_lst_com_measure"
        self.dim_comp_table = """
        ( 
                SELECT full_stock_id as comp_id
                ,stock_id
                ,nvl(abbr_cn,company_name_cn) company_abbr
                ,industry_level1 as industry_name
                FROM dim_china_listed_company 
                WHERE pt = MAX_PT('dim_china_listed_company')
        )
        """
        self.comp_type = "lst_com"
        self._index_var: List[VariableMap] = []
        # total count of source
        self._index_base: List[VariableMap] = []
        self._matrix_var: List[VariableMap] = []
        self.start_year = 2016
        self.end_year = 2020
        self._other_var: Dict[str, VariableMapOther] = {}
        self.comp_ids = []
        """empty for all comp_ids, default is all comp_ids"""

    def _get_index_cols(self):
        return (
            "," + "\n,".join([x.column_name or x.code for x in self._index_var])
            if self._index_var
            else ""
        )

    def _get_index_fields(self):
        return "\n,".join(
            f"'{x.code}' as {x.column_name or x.code}" for x in self._index_var
        )

    def _get_index_codes(self):
        return ",".join([f"'{x.code}'" for x in self._index_var])

    def _get_base_index_cols(self):
        return (
            "," + "\n,".join([x.column_name or x.code for x in self._index_base])
            if self._index_base
            else ""
        )

    def _get_base_index_fields(self):
        return "\n,".join(
            f"'{x.code}-total' as {x.column_name or x.code}" for x in self._index_base
        )

    def _get_matrix_fields(self):
        return "\n,".join(
            f"'{x.code}' as {x.column_name or x.code}" for x in self._matrix_var
        )

    def _get_matrix_cols(self):
        return (
            "," + ",".join([x.column_name or x.code for x in self._matrix_var])
            if self._matrix_var
            else ""
        )

    def _get_matrix_codes(self):
        return ",".join([f"'{x.code}'" for x in self._matrix_var])

    def add_index(self, code: str, column_name: Optional[str] = None):
        """add index data to panel

        Args:
            code (str): index code to add to panel's variable
            column_name (Optional[str], optional): if not provide, use code as column_name. Defaults to None.
        """
        self._index_var.append(VariableMap(code, column_name or code))

    def add_source_base(
        self,
        source_class: Type[CommonIndexGenerator],
        column_name: Optional[str] = None,
    ):
        self._index_base.append(
            VariableMap(
                source_class.get_source_name(),
                column_name or source_class.get_source_name(),
            )
        )

    def add_matrix(self, code: str, column_name: Optional[str] = None):
        self._matrix_var.append(VariableMap(code, column_name or code))

    def _get_com_year_squence_sql(self):
        return f"""(select /*+ MAPJOIN(y) */ * from 
        {self.dim_comp_table} a join {self._get_year_sequence()} y
        where {self._get_comp_condition()}
        )"""

    def _get_index_sql(self):
        if self._index_var:
            sql = f"""(SELECT * from
            ( select comp_id,eff_year,index_code,index_value from {self.index_dwd_table}  
                where index_version = '{self.index_version}'  
                and comp_type = '{self.comp_type}'
                and eff_year in {self._get_year_sequence()} and {self._get_comp_condition()}
                and index_code in ({self._get_index_codes()})
                )
            pivot (max(index_value) for index_code IN ({self._get_index_fields()}))
            )
            """
            return sql
        else:
            return ""

    def _get_base_index_sql(self):
        if self._index_base:
            sql = f"""(SELECT * from
        ( select comp_id,eff_year,index_version,index_value from {self.index_dwd_table}  
            where comp_type = '{self.comp_type}'
            and eff_year in {self._get_year_sequence()} and {self._get_comp_condition()}
            and index_code ='ttl_cnt'
            )
        pivot (max(index_value) for index_version IN ({self._get_base_index_fields()}))
        )
        """
            return sql
        else:
            return ""

    def _get_matrix_sql(self):
        if not self._matrix_var:
            return ""
        sql = f"""(SELECT * from 
            (select full_stock_id as comp_id,eff_year,source_code,measure_value from {self.matrix_dwd_table} 
             where eff_year in {self._get_year_sequence()} 
             and {self._get_comp_condition("full_stock_id")}
             and source_code in ({self._get_matrix_codes()})
            )
            pivot (max(measure_value) for source_code IN ({self._get_matrix_fields()}))
            )
        """
        return sql

    def _get_year_sequence(self):
        return f"(SELECT EXPLODE(SEQUENCE({self.start_year},{self.end_year})) as (eff_year))"

    def _get_comp_condition(self, comp_id_col="comp_id"):
        return (
            f""" {comp_id_col} in ({','.join([f"'{x}'" for x in self.comp_ids])})"""
            if self.comp_ids
            else "1=1"
        )

    def get_panel_sql(self):
        if self.index_version == "":
            raise Exception("index_version not set")
        if self.comp_type == "":
            raise Exception("comp_type not set")
        idx_sql = self._get_index_sql()
        base_idx_sql = self._get_base_index_sql()
        idx_join_sql = (
            f"""\nleft join {idx_sql} b 
        on a.comp_id =b.comp_id and a.eff_year=b.eff_year"""
            if idx_sql
            else ""
        )
        base_join_sql = (
            f"""\nleft join {base_idx_sql} d
        on a.comp_id =d.comp_id and a.eff_year=d.eff_year"""
            if base_idx_sql
            else ""
        )
        matrix_sql = self._get_matrix_sql()
        matrix_join_sql = (
            f"""\nleft join {matrix_sql} c  
        on a.comp_id =c.comp_id and a.eff_year=c.eff_year"""
            if matrix_sql
            else ""
        )

        other_vars = self._get_other_var_sql()
        other_vars_join_sql = "\n".join(
            [""]
            + [
                f"""left join {x} as {v} on {v}.comp_id = a.comp_id {f'and {v}.eff_year = a.eff_year' 
                if self._other_var[v].col_year else ''}"""
                for v, x in other_vars.items()
            ]
        )
        other_vars_cols = (
            "," + "\n,".join([f"{v}.{v}" for v, _ in other_vars.items()])
            if other_vars
            else ""
        )
        if (
            not idx_join_sql
            and not base_join_sql
            and not matrix_join_sql
            and not other_vars_cols
        ):
            raise Exception("please add at least one variable!")
        sql = f""" select a.comp_id,a.eff_year,a.company_abbr,a.industry_name
        {self._get_matrix_cols()}
        {self._get_base_index_cols()}
        {self._get_index_cols()}
        {other_vars_cols}
        from {self._get_com_year_squence_sql()} a
        {idx_join_sql}{base_join_sql} {matrix_join_sql}{other_vars_join_sql}
        ;
        """
        return sql

    def add_other_var(self, var_map: VariableMapOther):
        if self._other_var.get(var_map.var_col_name or var_map.source_var_col):
            raise Exception(
                f"other var {var_map.var_col_name or var_map.source_var_col} already exists"
            )
        self._other_var[var_map.var_col_name or var_map.source_var_col] = var_map

    def _get_other_var_sql(self):
        other_var_sql: Dict[str, str] = {}
        for x, v in self._other_var.items():
            eff_year = f" a.{v.col_year} as eff_year," if v.col_year else ""
            where = (
                f" where  {v.col_year} in {self._get_year_sequence()}"
                if v.col_year
                else ""
            )
            other_var_sql[x] = (
                f"""(
            SELECT  b.comp_id,{eff_year}a.{x}
            from (
                select {v.col_comp_id},{v.col_year+',' if v.col_year else ""}{v.source_var_col} as {x} from {v.source_data} {where}
            ) a join {self.dim_comp_table} b on {v.col_comp_id} = b.{v.dim_comp_id})
            """
            )
        return other_var_sql

    def get_result_df(self):
        sql = self.get_panel_sql()
        result = SqlRunner(sql).to_pandas()
        return result

    def save_to_csv(self, path):
        df = self.get_result_df()
        df.to_csv(path, index=False)
