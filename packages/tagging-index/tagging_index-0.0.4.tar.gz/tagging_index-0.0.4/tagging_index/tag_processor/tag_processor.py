from datetime import datetime
import json
from typing import Optional
import numpy as np
from odps import DataFrame
import pandas as pd

from data2cloud.cloud.maxcompute import SqlRunner
from .tag_validator import TagValidator
from tagging_index.utils.tag_tree import TagTree
from tagging_index._udf.tag_converter import TagConverter, TagStandardizer


class TagProcessor:
    def __init__(self):
        """
        process:
        1. load new config from folder should include 3 files:
            - tag_list.csv
            - prefix.csv
            - suffix.csv
            or load from json
            you can append more than one new config

        ```python
        >>> processor = TagProcessor()
        >>> processor.append_new_config_csv(tag_config_folder)
        >>> processor.append_new_config_json(tag_config_json_file)
        ```
        2. load current config from odps dim table or from local json file, if not specified, not compare with current config
        ```python
        >>> processor.load_current_config()
        >>> processor.load_local_current_config(current_config_file)
        ```
        3. validate the config and return log
        ```python
        >>> log = processor.validate_config()
        ```
        4. save the new config to odps dim table or json file. make sure all error fixed before save
        ```python
        >>> processor.save_to_json(file_name)
        >>> processor.save_to_version()
        ```
        """
        self._converter = TagConverter()
        self._standardizer = TagStandardizer()
        self._current_tags = None
        self._new_tags = []
        self.tree: TagTree = TagTree([])
        self._merge_current_config = True

    def append_new_config_csv(self, file_path: str):
        """load the raw tag config file and basic check. file_path should include 3 files:
        - tag_list.csv
        - prefix.csv
        - suffix.csv
        """
        df = self._raw_csv_to_df(file_path)
        config = self._converter.df_to_config(df)
        self._new_tags.extend(config)

    def append_new_config_json(self, file: str):
        """load the raw tag config file and basic check"""
        config = self._converter.dict_to_config(json.load(open(file)))
        self._new_tags.extend(config)

    def load_current_config(self, version: str = ""):
        """load current config from odps dim table, if version is not specified, load the latest version

        Args:
            version (str, optional): _description_. Defaults to "".
        """
        self._current_tags = self._converter.df_to_config(
            self._converter.version_to_df(version)
        )

    def load_local_current_config(self, config_file: str):
        """load current config from local config file, load_current_config and load_local_current_config are mutually exclusive

        Args:
            config_file (str): json file config
        """
        with open(config_file, "r") as file:
            current_config_dict = json.load(file)
            self._current_tags = self._converter.dict_to_config(current_config_dict)

    def _raw_csv_to_df(self, file_path: str):
        """convert local csv raw tag config to df
        Args:
            file_path (str): file_path must include and only include 3 files: tag_list.csv, prefix.csv, suffix.csv
        """
        import pandas as pd

        tag_list = pd.read_csv(filepath_or_buffer=f"{file_path}/tag_list.csv")
        # TagValidator.check_duplicated_tags(tag_list, True)
        prefix_list = pd.read_csv(f"{file_path}/prefix.csv")
        suffix_list = pd.read_csv(f"{file_path}/suffix.csv")
        tag_list = tag_list[
            [
                "tag",
                "parent_tag",
                "is_keyword",
                "data_phase",
                "category",
                "language",
            ]
        ]
        prefix_list = prefix_list[["tag", "kw", "data_phase", "category", "distance"]]
        suffix_list = suffix_list[["tag", "kw", "data_phase", "category", "distance"]]
        std = TagStandardizer()
        self._tag_list = std.apply_df(tag_list)
        self._prefix_list = std.apply_df(prefix_list)
        self._suffix_list = std.apply_df(suffix_list)
        return self._merge_prefix_suffix(tag_list, prefix_list, suffix_list)

    def reset_conifg(self):
        self._current_tags = None
        self._new_tags = []
        self.tree = TagTree([])

    def _merge_prefix_suffix(
        self, tag_df: pd.DataFrame, prefix_df: pd.DataFrame, suffix_df: pd.DataFrame
    ):
        import pandas as pd

        prefix_aggregated = (
            pd.DataFrame()
            if prefix_df.empty
            else prefix_df.groupby("tag")
            .apply(
                lambda x: x[["kw", "distance", "category", "data_phase"]].to_dict(
                    "records"
                ),
                include_groups=False,
            )
            .reset_index(name="prefix")
        )
        suffix_aggregated = (
            pd.DataFrame()
            if suffix_df.empty
            else (
                suffix_df.groupby("tag")
                .apply(
                    lambda x: x[["kw", "distance", "category", "data_phase"]].to_dict(
                        "records"
                    ),
                    include_groups=False,
                )
                .reset_index(name="suffix")
            )
        )
        # Ensure 'parent_tags' is a list of strings, not a single string
        if "parent_tag" in tag_df.columns:
            tag_df["parent_tags"] = tag_df["parent_tag"].apply(
                lambda x: [x] if pd.notna(x) else []
            )
            tag_df.drop("parent_tag", axis=1, inplace=True)
        # Merge prefix and suffix data into the tag dataframe
        if not prefix_aggregated.empty:
            tag_df = tag_df.merge(prefix_aggregated, on="tag", how="left")
        else:
            tag_df["prefix"] = None
        if not suffix_aggregated.empty:
            tag_df = tag_df.merge(suffix_aggregated, on="tag", how="left")
        else:
            tag_df["suffix"] = None
        tag_df.replace(np.nan, None, inplace=True)
        return tag_df

    def validate(self):
        """compare the raw tag config file with certain version's existing tags
        1. check duplicated tags
        2. check parent hierarchy
        3. check tag update difference
        4. check tag match overlap
        Args:
            version (str, optional): _description_. Defaults to "", use latest version.
        return dict: {
            "summary": { err_cnt:int,new_tag_cnt:int,update_tag_cnt:int },
            "dupldated_tags": [],
            "missed_parents": [],
            "circular_references": [path],
            "overlap_config": {tag:[tag...]},
            "tag_update": {field: {tag: change}
            "new_tags": {tag:parent_tag}
            },
        }
        """

        validator = TagValidator(self._new_tags, self._current_tags)
        validator.check_tags()
        validator.validate_parent_hierarchy()
        validator.check_updated_config()
        validator.check_match_overlap()
        self.has_error = (
            validator.duplicated_tags
            or validator.missed_parents
            or validator.circular_references
            or validator.overlap_config
        )
        self.validator = validator
        err_cnt = (
            len(validator.duplicated_tags)
            + len(validator.missed_parents)
            + len(validator.circular_references)
            + len(validator.overlap_config)
        )
        # count distinct tag count from validate.tag_update's value dict keys
        update_tag_cnt = len({k for v in validator.tag_update.values() for k in v})
        # new tag cnt = new_config key not in current_config key
        new_tags = {
            k: v.parent_tags[0] if v.parent_tags else ""
            for k, v in validator.new_config.items()
            if k not in validator.current_config
        }
        new_tag_cnt = len(new_tags)
        return {
            "summary": {
                "err_cnt": err_cnt,
                "new_tag_cnt": new_tag_cnt,
                "update_tag_cnt": update_tag_cnt,
            },
            "dupldated_tags": validator.duplicated_tags,
            "missed_parents": validator.missed_parents,
            "circular_references": validator.circular_references,
            "overlap_config": validator.overlap_config,
            "tag_update": validator.tag_update,
            "new_tags": new_tags,
        }

    def save_to_json(self, output_file: str, merge_current_config: bool = True):
        self._converter.config_to_json(
            list(self.validator.get_valid_config(merge_current_config).values()),
            output_file,
        )

    def save_to_version(self, merge_current_config: bool = True):
        tmp_table = self.save_to_temp_table(merge_current_config)
        self._insert_partition(tmp_table, "dim_digitalization_tag")
        result = f"version:{self._tag_version}"
        return result

    def save_to_temp_table(self, merge_current_config: bool = True):
        merged_configs = self.validator.get_valid_config(merge_current_config)
        df = self._converter.config_to_df(list(merged_configs.values()))
        tmp_table = self._persist_tmp_table(self._standardizer.df_serialize(df))
        return tmp_table

    def show_tree(
        self, root_tag: Optional[str] = None, levels=0, merge_current_config=True
    ):
        """print the tag tree

        Args:
            root_tag (Optional[str], optional): print the sub tree of root_tag if specified. Defaults to None.
            levels (int, optional): how many levels to print from root_tag. Defaults to 0.
            merge_current_config (bool, optional): combine current config with new config and print. Defaults to True.
        """
        self._init_tree(merge_current_config)
        self.tree.show_level(root_tag, levels)

    def _init_tree(self, merge_current_config=True) -> None:
        if self._merge_current_config != merge_current_config:
            self.tree = TagTree([])
        if self.tree.size() == 0:
            config = self.validator.get_valid_config(merge_current_config)
            self.tree = TagTree(list(config.values()))

    # def find_tag(self, tag: str, merge_current_config=True):
    #     """find tag and show the tag path"""
    #     self._init_tree(merge_current_config)
    #     self.tree.show_level(tag, levels=1)

    def _persist_tmp_table(self, df: pd.DataFrame) -> str:
        now = datetime.now()
        # 格式化日期和时间
        formatted_date = now.strftime("%Y%m%d")
        formatted_time = now.strftime("%H%M%S").zfill(6)
        # 合并日期和时间
        tag_version = formatted_date + formatted_time
        df["tag_version"] = tag_version
        tmp_table_name = f"tmp_tag_{tag_version}"
        # 写表指定字符串
        as_type = {
            col: "string" if dtype != bool else dtype.name
            for col, dtype in df.dtypes.items()
        }
        odps_df = DataFrame(df, as_type=as_type)
        odps_df["tag"] = odps_df["tag"].replace(r"[\n\r\t]", "")
        # 写入分区表
        odps_df.persist(tmp_table_name, lifecycle=1)
        self._tag_version = tag_version
        return tmp_table_name

    def _insert_partition(self, tmp_table_name: str, target_table: str):
        sql = f"""
        INSERT OVERWRITE TABLE {target_table} PARTITION (tag_version)
            SELECT
            tag,
            cast(tag_level as int),
            from_json(prefix,"ARRAY<STRUCT<kw:STRING,distance:INT,category:STRING,data_phase:STRING>>"),
            from_json(suffix,"ARRAY<STRUCT<kw:STRING,distance:INT,category:STRING,data_phase:STRING>>"),
            cast(is_keyword as BOOLEAN),
            language,
            category,
            data_cycle,
            data_phase,
            from_json(parent_tags,"ARRAY<STRING>"),
            tag_version
            FROM {tmp_table_name} 
            ; 
            """
        # 同步执行
        SqlRunner(sql).run()
