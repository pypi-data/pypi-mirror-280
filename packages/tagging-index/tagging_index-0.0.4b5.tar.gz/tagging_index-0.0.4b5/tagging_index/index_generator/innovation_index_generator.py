from .common_index_generator import CommonIndexGenerator


class InnovationIndexGenerator(CommonIndexGenerator):
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
        with app_no as (
            SELECT distinct application_no
            ,SUBSTR(application_date,1,4) AS application_year from dwd_patent_desc 
            WHERE   pt = MAX_PT ('dwd_patent_desc') 
            and nullif(content,'') is not null
        )
        ,entity as (
            select distinct application_no,ic_usc_code as social_credit_code
            from dwd_patent_entity 
        LATERAL VIEW EXPLODE(ic_usc_codes) tmp AS ic_usc_code 
        where pt = MAX_PT('dwd_patent_entity') and ic_usc_code <>""
        )
        select social_credit_code as source_comp_id
                    ,a.application_no as entity_id
                    ,application_year as start_year
                    ,application_year as end_year
                    ,'total' as tag_udf_version
                    from app_no a join entity b on a.application_no=b.application_no
            )
        """
    __TABLE_SOURCE_LST_COM = "dwd_tag_patent_china"
    __sql_src_tag_lst_com = (
        """ (
            select social_credit_code as source_comp_id
            ,application_no as entity_id
            ,application_year as start_year
            ,application_year as end_year
            ,tag_udf_version
            from """
        + __TABLE_SOURCE_LST_COM
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
        return self.__TABLE_SOURCE_LST_COM

    def get_sql_source_tag_lst_com(
        self, tag_condition: str, tag_udf_version: str
    ) -> str:
        return self.__sql_src_tag_lst_com.format(
            **{
                "tag_udf_version": tag_udf_version,
                "tag_condition": tag_condition,
            }
        )

    @classmethod
    def get_source_name(cls):
        return "innovation"

    @classmethod
    def get_index_suffix(cls):
        return "I"
