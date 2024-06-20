import json
from typing import Optional, Tuple
from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class CurrentConfig:
    ignore: bool
    local_file: str
    odps_version: str


@dataclass
class ConfigData:
    csv: List[str]
    json: List[str]
    current_config: CurrentConfig


@dataclass
class ConfigOutput:
    log: str
    format: str
    output_file: str


@dataclass
class PreSuffixConfig:
    kw: str
    category: Optional[str] = field(default=None)
    data_phase: Optional[str] = field(default=None)
    distance: int = field(default=0)


@dataclass
class TagConfig:
    tag: str
    language: str
    tag_level: int
    parent_tags: List[str] = field(default_factory=list)
    is_keyword: Optional[bool] = field(default=False)
    prefix: List[PreSuffixConfig] = field(default_factory=list)
    suffix: List[PreSuffixConfig] = field(default_factory=list)
    category: Optional[str] = field(default=None)
    data_phase: Optional[str] = field(default=None)
    data_cycle: Optional[str] = field(default=None)


class TagConverter:
    def __init__(self):
        """convert tag config between raw csv, json file, odps version, config objects"""
        self.standardizer = TagStandardizer()

    def config_to_df(self, tag_configs: List[TagConfig]):
        """Convert the tag config list to a DataFrame. standardize format"""
        import pandas as pd

        df = pd.DataFrame(tag_configs)
        df = self.standardizer.apply_df(df)
        return df

    def df_to_json(self, dataframe, file_path):
        """Convert the DataFrame to JSON and save it to a json file."""
        # 动态导入,避免udf(不使用pandas) 引用时出错
        import pandas as pd

        df: pd.DataFrame = dataframe
        tag_dict = df.to_dict(orient="records")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tag_dict, file, ensure_ascii=False, indent=4)

    def config_to_json(self, tag_configs: List[TagConfig], file_path):
        df = self.config_to_df(tag_configs)
        self.df_to_json(df, file_path)

    def udf_res_to_config(self, table_res_name: str) -> Tuple[str, List[TagConfig]]:
        """convert resource table data to tag config, only for UDF env.

        Args:
            res_table (List[]): mc table resource data
            columns (List[str]): mc table resource column name list

        Returns:
            List[TagConfig]: tag config list
        """
        from odps.distcache import get_cache_table
        from odps.distcache import get_cache_tabledesc

        desc = list(get_cache_tabledesc(table_res_name))  # type: ignore
        data = list(get_cache_table(table_res_name))  # type: ignore
        columns = list(map(lambda x: x["name"], desc[2]))
        tag_version = data[0][columns.index("tag_version")] if len(data) > 0 else "NONE"

        tag_configs: List[TagConfig] = []
        for x in data:
            prefix_s = json.loads(
                x[columns.index("prefix")] if x[columns.index("prefix")] else "[]"
            )
            prefix = [
                PreSuffixConfig(x["kw"], x["category"], x["distance"]) for x in prefix_s
            ]
            suffix_s = json.loads(
                x[columns.index("suffix")] if x[columns.index("suffix")] else "[]"
            )
            suffix = [
                PreSuffixConfig(x["kw"], x["category"], x["distance"]) for x in suffix_s
            ]
            parent_tags = json.loads(
                x[columns.index("parent_tags")]
                if x[columns.index("parent_tags")]
                else "[]"
            )
            tc = TagConfig(
                x[columns.index("tag")],
                x[columns.index("language")],
                x[columns.index("tag_level")],
                parent_tags,
                x[columns.index("is_keyword")],
                prefix,
                suffix,
                x[columns.index("category")],
                x[columns.index("data_phase")],
                x[columns.index("data_cycle")],
            )
            tag_configs.append(tc)
        return tag_version, tag_configs

    def dict_to_config(self, dict: List[Dict]) -> List[TagConfig]:
        """convert Dict to tag config

        Returns:
            List[TagConfig]: tag config list
        """
        tag_configs: List[TagConfig] = []
        for x in dict:
            prefix = self._dict_to_fixConfig(x["prefix"])
            suffix = self._dict_to_fixConfig(x["suffix"])
            tc = TagConfig(
                x["tag"],
                x["language"],
                x["tag_level"],
                x["parent_tags"],
                x["is_keyword"],
                prefix,
                suffix,
                x["category"],
                x["data_phase"],
                x["data_cycle"] if x.keys().__contains__("data_cycle") else None,
            )
            tag_configs.append(tc)
        return tag_configs or []

    def version_to_config(self, version=""):
        """read certain version from opds tag dim table, if version="", use the latest version

        Args:
            version (str, optional): tag version. Defaults to "",use latest version.
        """
        df_tags = self.version_to_df(version)
        return self.df_to_config(df_tags)

    def version_to_df(self, version=""):
        """read certain version from opds tag dim table, if version="", use the latest version

        Args:
            version (str, optional): tag version. Defaults to "",use latest version.
        """
        import pandas as pd
        from data2cloud.cloud.maxcompute import SqlRunner

        dim_table = "dim_digitalization_tag"
        version = f'"{version}"' if version else f'max_pt("{dim_table}")'
        sql = f"select * from {dim_table}  where tag_version={version}"
        sql_runner = SqlRunner(sql)
        df_tags: pd.DataFrame = sql_runner.to_pandas()
        return df_tags

    def df_to_config(self, df_tags) -> List[TagConfig]:
        """convert dataframe to tag config

        Args:
            df_tags (pd.DataFrame): dataframe

        Returns:
            List[TagConfig]: tag config list
        """
        tag_configs: List[TagConfig] = []
        for _, row in df_tags.iterrows():
            prefix = self._dict_to_fixConfig(row["prefix"])
            suffix = self._dict_to_fixConfig(row["suffix"])
            tc = TagConfig(
                row["tag"],
                row["language"],
                len(row["parent_tags"] if row["parent_tags"] else []) + 1,
                row["parent_tags"],
                row["is_keyword"],
                prefix,
                suffix,
                row["category"],
                row["data_phase"],
            )
            tag_configs.append(tc)
        return tag_configs

    def _dict_to_fixConfig(self, dict: List[Dict]) -> List[PreSuffixConfig]:

        presuffix = [
            PreSuffixConfig(p["kw"], p["category"], p["data_phase"], p["distance"])
            for p in (dict if dict else [])
        ]
        return presuffix


class TagStandardizer:
    def __init__(self):
        pass

    @staticmethod
    def serialize(val):
        if (
            isinstance(val, list)
            and len(val) > 0
            and isinstance(val[0], PreSuffixConfig)
        ):
            return json.dumps(
                [x.__dict__ for x in val], ensure_ascii=False
            )  # Implement a to_dict method in PreSuffixConfig
        else:
            return (
                json.dumps(val, ensure_ascii=False)
                if isinstance(val, dict) or isinstance(val, list)
                else val
            )

    @staticmethod
    def standardize_value(value):
        """Standardize a single value by stripping, converting to lower case, etc."""
        if isinstance(value, str):
            return value.strip()
        return value

    def df_serialize(self, dataframe):
        for column in dataframe.columns:
            dataframe[column] = dataframe[column].apply(self.serialize)
        return dataframe

    def apply_df(self, dataframe):
        """Apply standardization to each column in the dataframe."""
        for column in dataframe.columns:
            dataframe[column] = dataframe[column].apply(self.standardize_value)
        return dataframe

    def apply_config(self, tag_config: List[TagConfig]):
        """Apply standardization to each tag,prefix.kw,suffix.kw in the list."""
        for t in tag_config:
            t.tag = self.standardize_value(t.tag)
            for p in t.prefix or []:
                p.kw = self.standardize_value(p.kw)
            for s in t.suffix or []:
                s.kw = self.standardize_value(s.kw)
            t.parent_tags = (
                [self.standardize_value(p) for p in t.parent_tags]
                if t.parent_tags
                else []
            )
        return tag_config
