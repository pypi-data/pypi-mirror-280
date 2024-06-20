from .common_index_generator import CommonIndexGenerator


class DemandIndexGenerator(CommonIndexGenerator):
    # overload the baseclass
    _sql_comp_map_lst_com = """ ( 
        SELECT  distinct full_stock_id AS comp_id
            ,tmp.source_comp_id
            ,nvl(abbr_cn,company_name_cn) company_abbr
            FROM    dim_china_listed_company a
            LATERAL VIEW EXPLODE(social_credit_codes) tmp AS source_comp_id
                WHERE pt = MAX_PT('dim_china_listed_company')
            )
        """
    __sql_src_ttl_lst_com = """ (
        select social_credit_code as source_comp_id
            ,job_id as entity_id
            ,pt as start_year
            ,pt as end_year
            ,'total' as tag_udf_version
            from dwd_scc_com_job_posting
            where pt>'2015'
            )
        """
    _TABLE_SOURCE_LST_COM = "dwd_tag_scc_com_job_posting"
    _sql_src_tag_lst_com = (
        """ (
            select social_credit_code as source_comp_id
            ,job_id as entity_id
            ,activity_year as start_year
            ,activity_year as end_year
            ,tag_udf_version
            from """
        + _TABLE_SOURCE_LST_COM
        + """
            where tag_udf_version = {tag_udf_version}
            and {tag_condition}
            )
        """
    )

    @property
    def _sql_src_ttl_lst_com(self):
        return self.__sql_src_ttl_lst_com

    @property
    def _table_source_tag_lst_com(self):
        return self._TABLE_SOURCE_LST_COM

    def get_sql_source_tag_lst_com(
        self, tag_condition: str, tag_udf_version: str
    ) -> str:
        return self._sql_src_tag_lst_com.format(
            **{
                "tag_udf_version": tag_udf_version,
                "tag_condition": tag_condition,
            }
        )

    @classmethod
    def get_source_name(cls):
        return "demand"

    @classmethod
    def get_index_suffix(cls):
        return "D"
