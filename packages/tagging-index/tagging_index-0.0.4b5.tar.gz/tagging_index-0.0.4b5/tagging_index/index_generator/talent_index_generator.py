from .common_index_generator import CommonIndexGenerator


class TalentIndexGenerator(CommonIndexGenerator):
    # define the sql template as static property

    __sql_src_ttl_lst_com = """(
            select full_stock_id as source_comp_id
            ,user_id as entity_id
            ,start_year
            ,end_year
            ,'total' as tag_udf_version
            from dwd_cn_lst_com_pos_linkedin
            where end_year>2000
            )
        """
    __TABLE_SOURCE_LST_COM = "dwd_tag_lst_com_linkedin_position_skill"
    _sql_src_tag_lst_com = (
        """(
            select full_stock_id as source_comp_id
            ,user_id as entity_id
            ,hire_year as start_year
            ,dismiss_year as end_year
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
        return self._sql_src_tag_lst_com.format(
            **{
                "tag_udf_version": tag_udf_version,
                "tag_condition": tag_condition,
            }
        )

    @classmethod
    def get_source_name(cls):
        return "talent"

    @classmethod
    def get_index_suffix(cls):
        return "T"
