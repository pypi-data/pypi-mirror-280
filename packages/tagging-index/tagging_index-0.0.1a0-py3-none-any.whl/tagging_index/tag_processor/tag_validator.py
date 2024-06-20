from typing import List, Optional
import pandas as pd

from tagging_index._udf.tag_converter import (
    TagStandardizer,
    PreSuffixConfig,
    TagConfig,
    TagConverter,
)
from tagging_index._udf.tag_matcher import TagMatcher


class TagValidator:
    def __init__(
        self,
        new_conf_list: List[TagConfig],
        cur_conf_list: Optional[List[TagConfig]] = None,
    ):
        """validate new config with current config if provide

        Args:
            new_config (List[TagConfig]): new tag config
            current_config (Optional[List[TagConfig]], optional): the current tag config. Defaults to None. if not provide, will use new_config as current_config
        """
        self.stanadardizer = TagConverter()
        self.new_config_list = new_conf_list
        self.current_config_list = cur_conf_list or new_conf_list
        self.has_current_config = cur_conf_list is not None
        # convert list to dict with tag as key, last win if dup.
        self.new_config = {n.tag: n for n in self.new_config_list}
        self.current_config = {n.tag: n for n in self.current_config_list}
        self.updated_config = {}

    @staticmethod
    def check_duplicated_tags(df_tags: pd.DataFrame, raise_err=False):
        if df_tags.empty:
            return []
        if "tag" not in df_tags.columns:
            raise ValueError("DataFrame must contain a 'tag' column")
        # check column tag if duplicated and find all duplicates
        # standardize tag name before check
        df_tags["tag"] = df_tags["tag"].apply(lambda x: x.strip().lower())
        duplicates = df_tags.duplicated(subset="tag")
        dup_tags = list(set(df_tags[duplicates]["tag"]))
        if duplicates.any() and raise_err:
            raise ValueError(f"duplicated tag(s) found: {','.join(dup_tags)}")
        return dup_tags

    def check_tags(self):
        """check new config and current config's tag, return duplicated tags, missed parent tags

        Raises:
            ValueError: for current config will raise err directly

        Returns:
            (list[str],list[str]): (duplicated tags,missed parents) for new config
        """
        if self.has_current_config:
            dup_tags = self.check_duplicated_tags(
                pd.DataFrame(self.current_config_list)
            )
            if len(dup_tags) > 0:
                raise ValueError(
                    f"duplicated tag(s) found in current config: {','.join(dup_tags)}"
                )
        duplicated_tags = self.check_duplicated_tags(pd.DataFrame(self.new_config_list))
        missed_parents = self.build_tag_hierarchy()
        self.duplicated_tags = duplicated_tags
        # print(self.tag_hierarchy, self.current_tag_hierarchy)
        return (duplicated_tags, missed_parents)

    # compare prefix and suffix with serialized json
    @staticmethod
    def compare_field(new, cur):
        new = TagStandardizer.serialize(new)
        cur = TagStandardizer.serialize(cur)
        # only compare when new is not None
        if new and (new != cur):
            return f"{cur}->{new}"

    def check_updated_config(self):
        """compare the new tag config with current tag config"""
        field_list = [
            "is_keyword",
            "data_phase",
            "category",
            "data_cycle",
            "language",
        ]
        # use field_list as key for updated_config dict
        updated_config = {k: {} for k in field_list}
        updated_config["prefix"] = {}
        updated_config["suffix"] = {}

        if self.has_current_config:
            for tag, new_conf in self.new_config.items():
                if tag in self.current_config:
                    cur_conf = self.current_config[tag]
                    self.updated_config[tag] = new_conf
                    # Check for update
                    for field in field_list:
                        u = self.compare_field(
                            new_conf.__dict__[field], cur_conf.__dict__[field]
                        )
                        if u:
                            updated_config[field][tag] = u

                    # check prefix and suffix for current tag
                    updated_prefix, merged_prefix = self.check_updated_fix(
                        tag, new_conf.prefix, cur_conf.prefix
                    )
                    if updated_prefix:
                        updated_config["prefix"].update(updated_prefix)
                        # merge fix at same tag
                        self.updated_config[tag].prefix = list(merged_prefix.values())
                    updated_suffix, merged_suffix = self.check_updated_fix(
                        tag, new_conf.suffix, cur_conf.suffix
                    )
                    if updated_suffix:
                        updated_config["suffix"].update(updated_suffix)
                        self.updated_config[tag].suffix = list(merged_suffix.values())

        # check parent tags, only the first element
        updated_config["parent_tag"] = self.check_updated_parents()
        # remove empty values
        updated_config = {k: v for k, v in updated_config.items() if v}
        self.tag_update = updated_config
        return updated_config

    def check_updated_fix(
        self, tag: str, new_fix: List[PreSuffixConfig], cur_fix: List[PreSuffixConfig]
    ):
        """check prefix or suffix update, new add or config change, TODO remove kw
        Returns:
            {tag:updated_fix}
        """
        updated_fix = {"update": {}, "new": [], "remove": []}
        merged_fix = {p.kw: p for p in cur_fix}
        field_list = ["category", "distance", "data_phase"]
        new_fix_dict = {x.kw: x for x in new_fix}
        cur_fix_dict = {x.kw: x for x in cur_fix}
        if self.has_current_config and new_fix:
            for kw, new_conf in new_fix_dict.items():
                if kw in cur_fix_dict:
                    cur_conf = cur_fix_dict[kw]
                    # Check for update
                    updated = []
                    for field in field_list:
                        u = self.compare_field(
                            new_conf.__dict__[field], cur_conf.__dict__[field]
                        )
                        if u:
                            updated.append(u)
                            # update merged_fix
                            merged_fix[kw].__dict__[field] = new_conf.__dict__[field]
                    if updated:
                        updated_fix["update"][kw] = updated
                else:
                    updated_fix["new"].append(new_conf.__dict__)
                    # append merged_fix
                    merged_fix[kw] = new_conf
        updated_fix = {k: v for k, v in updated_fix.items() if v}
        return {tag: updated_fix} if updated_fix else {}, merged_fix

    def check_updated_parents(self):
        updated_parents = {}
        if self.has_current_config:
            for tag in self.tag_hierarchy:
                if tag in self.current_tag_hierarchy:
                    if self.current_tag_hierarchy[tag] != self.tag_hierarchy[tag]:
                        updated_parents[tag] = (
                            f"{self.current_tag_hierarchy[tag]}->{self.tag_hierarchy[tag]}"
                        )
        self.updated_parents = updated_parents
        return updated_parents

    def build_tag_hierarchy(self):
        """build hierarchy for new config, refer to current config if exists
            initialize self's tag_hierarchy,current_tag_hierarchy,missed_parents
        Returns:
            list[str]: missed_parents
        """
        missed_parents = set()
        # based on new config and current config to build new tag's hierarchy
        tag_hierarchy = self.get_tag_parent_pair(self.new_config_list)
        current_tag_hierarchy = self.get_tag_parent_pair(self.current_config_list)
        # check if all parent tag is in hierarchy, if not check in current config's tag
        for parent_tag in list(tag_hierarchy.values()):
            if parent_tag and parent_tag not in tag_hierarchy:
                if parent_tag in current_tag_hierarchy:
                    tag_hierarchy[parent_tag] = current_tag_hierarchy[parent_tag]
                else:
                    # record error str, return all errors
                    missed_parents.add(parent_tag)
        self.missed_parents = list(missed_parents)
        self.tag_hierarchy = tag_hierarchy
        self.current_tag_hierarchy = current_tag_hierarchy
        return self.missed_parents

    @staticmethod
    def get_tag_parent_pair(config: List[TagConfig]):
        hierarchy = {}
        for tag_config in config:
            hierarchy[tag_config.tag] = (
                tag_config.parent_tags[0] if tag_config.parent_tags else ""
            )
        return hierarchy

    def validate_parent_hierarchy(self):
        """append parent full path and level and Check for circular dependencies in tag parent-child relationships."""
        # check cycle in tag hierarchy
        circular_references = set()
        circular_tags = []
        for tag, config in self.new_config.items():
            p = config.parent_tags[0] if config.parent_tags else ""
            # include tag self to check for cycle
            tag_path = [tag]
            while p:
                tag_path.append(p)
                p = self.tag_hierarchy[p] if p in self.tag_hierarchy else ""
                if p in tag_path:
                    # already exist circular Parent tag
                    if p not in circular_tags:
                        circular_tags.append(p)
                        short_path = [t for t in tag_path[tag_path.index(p) :]]
                        short_path.append(p)
                        circular_references.add("->".join(short_path))
                    break
            # remove tag itself
            self.new_config[tag].parent_tags = tag_path[1:]
            self.new_config[tag].tag_level = len(tag_path)
        self.circular_references = list(circular_references)
        return self.circular_references

    def get_valid_config(self, merge_current_config: bool = True):

        merged_configs = self.new_config.copy()

        if merge_current_config and self.has_current_config:
            for tag in merged_configs:
                if tag in self.updated_config:
                    merged_configs[tag] = self.updated_config[tag]
            # new config'tag will override current config'tag
            append_current = {
                k: v for k, v in self.current_config.items() if k not in self.new_config
            }
            merged_configs.update(append_current)
        return merged_configs

    def check_match_overlap(self):
        self.matcher = TagMatcher()
        overlap_config = {}
        valid_config = self.get_valid_config()
        self.matcher.load_tags(list(valid_config.values()))

        for tag, conf in valid_config.items():
            if conf.is_keyword:
                match_results = self.matcher.match_content(tag)
                if len(match_results) > 1:
                    # 排除tag自身
                    for x in match_results:
                        if x.tag != tag:
                            if x.tag not in overlap_config:
                                overlap_config[x.tag] = set()
                            overlap_config[x.tag].add(tag)
        # change set to list
        for tag in overlap_config:
            overlap_config[tag] = list(overlap_config[tag])
        self.overlap_config = overlap_config
        return overlap_config
