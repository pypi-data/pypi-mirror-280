from collections import Counter

import re
from typing import List, Dict, Optional
from dataclasses import dataclass, field

from .tag_converter import (
    PreSuffixConfig,
    TagConfig,
    TagStandardizer,
)


@dataclass
class TagMatch:
    prefix: Optional[str]
    suffix: Optional[str]
    p_distance: int
    s_distance: int
    tag: str
    language: str
    tag_level: int
    match_length: int
    category: Optional[str]
    data_phase: Optional[str]
    data_cycle: Optional[str]
    parent_tags: List[str]
    basic_match: str
    pattern: Optional[re.Pattern] = field(default=None)


@dataclass
class MatchResult:
    prefix: Optional[str]
    suffix: Optional[str]
    tag: str
    category: Optional[str]
    data_phase: Optional[str]
    data_cycle: Optional[str]
    matched: str


class TagMatcher:
    def __init__(self):
        self.tag_config: Dict[str, TagConfig] = {}
        self.tag_match_list: List[TagMatch] = []
        self.standardizer = TagStandardizer()

    def load_tags(self, tag_data: List[TagConfig]):
        tc_list = self.standardizer.apply_config(tag_data)
        tc_dict = {i.tag: i for i in tc_list}
        # Inherit parent tag settings by sorting based on tag level
        sorted_configs = sorted(tc_dict.values(), key=lambda tm: tm.tag_level)
        for p in sorted_configs:
            for parent_tag in p.parent_tags:
                if parent_tag in tc_dict:
                    self.merge_parent_configs(p, tc_dict[parent_tag])
        self.tag_config = tc_dict
        self.tag_match_list = self.parse_tag_match()

    def parse_tag_match(self) -> List[TagMatch]:
        tag_list: List[TagMatch] = []
        for p in self.tag_config.values():
            if p.is_keyword:
                basic_match = f" {p.tag} " if p.language == "EN" else p.tag
                match_length = len(basic_match.strip())
                tag_list.append(
                    TagMatch(
                        None,
                        None,
                        0,
                        0,
                        p.tag,
                        p.language,
                        p.tag_level,
                        match_length,
                        p.category,
                        p.data_phase,
                        p.data_cycle,
                        p.parent_tags,
                        basic_match,
                    )
                )
            for pre_config in p.prefix or []:
                tag_list.extend(self.parse_tag_pre_suffix(p, pre_config, True))
            for suf_config in p.suffix or []:
                tag_list.extend(self.parse_tag_pre_suffix(p, suf_config, False))

        # Sort by tag level and presence of prefix/suffix
        sorted_tag_list = sorted(
            tag_list,
            key=lambda tm: (
                -tm.tag_level,
                (-1 if tm.prefix else 0) + (-1 if tm.suffix else 0),
            ),
        )
        return sorted_tag_list

    def parse_tag_pre_suffix(
        self, tc: TagConfig, config: PreSuffixConfig, is_pre: bool
    ) -> List[TagMatch]:
        """
        Parses a single prefix or suffix configuration and returns a list of TagMatch objects.

        Args:
            param (TagConfig): The main tag configuration.
            config (PreSuffixConfig): The prefix or suffix configuration to be parsed.
            is_pre (bool): Whether the configuration is for a prefix.

        Returns:
            List[TagMatch]: A list of TagMatch objects representing the parsed configuration.
        """

        def fix_pattern_cn(prefix, distance, suffix):
            pattern = r"{}[^\W\s_]{{{}}}{}".format(
                prefix, "{},{}".format(0, distance), suffix
            )
            return re.compile(pattern)

        def fix_pattern_en(prefix, distance, suffix):
            # 构造正则表达式，允许0-distance个单词（由[a-zA-Z]*\s*表示）在prefix和keyword之间
            pattern = r"(?i)\b{}\b(?:\s*[a-zA-Z.-]*\s*){{{}}}\b{}".format(
                prefix, "{},{}".format(0, distance), suffix
            )
            # print(pattern)
            return re.compile(pattern)

        # 模式匹配前缀和后缀, 根据当前配置是否pre决定
        pattern_pre = config.kw if is_pre else tc.tag
        pattern_suf = tc.tag if is_pre else config.kw
        # 根据中英文决定匹配方式
        basic_pattern = " {} {} " if tc.language == "EN" else "{}{}"
        fix_pattern = fix_pattern_cn if tc.language == "CN" else fix_pattern_en
        basic_match = None
        pattern = None
        # 如果距离=0 则用简单匹配
        basic_match = basic_pattern.format(pattern_pre, pattern_suf)
        if config.distance > 0:
            pattern = fix_pattern(pattern_pre, config.distance, pattern_suf)
        match_len = len(basic_match.strip())
        match = TagMatch(
            config.kw if is_pre else None,
            None if is_pre else config.kw,
            config.distance if is_pre else 0,
            0 if is_pre else config.distance,
            tc.tag,
            tc.language,
            tc.tag_level,
            match_len,
            config.category or tc.category,
            config.data_phase or tc.data_phase,
            tc.data_cycle,
            tc.parent_tags,
            basic_match,
            pattern,
        )
        return [match]

    def merge_parent_configs(self, current: TagConfig, parent: TagConfig) -> None:
        """
        Merges the prefix and suffix configurations from the parent TagConfig into the current one.

        Args:
            current (TagConfig): The child TagConfig to update.
            parent (TagConfig): The parent TagConfig providing additional configurations.
        """
        for pre_config in parent.prefix:
            if pre_config.kw not in [c.kw for c in current.prefix]:
                current.prefix.append(pre_config)
        for suf_config in parent.suffix:
            if suf_config.kw not in [c.kw for c in current.suffix]:
                current.suffix.append(suf_config)

    def get_tag_range(self, p_tag_range: List[str]) -> List[TagMatch]:
        p_tag_range = [x.lower() for x in p_tag_range]
        tag_configs: Dict[str, TagConfig] = {}

        # 一级标签
        for tag, config in self.tag_config.items():
            if tag in p_tag_range:
                tag_configs[tag] = config

        # 二级及更高级别的标签
        processed_tags = set(tag_configs.keys())
        while True:
            new_tags_added = False
            for tag, config in self.tag_config.items():
                if tag not in processed_tags and any(
                    parent in processed_tags for parent in config.parent_tags
                ):
                    tag_configs[tag] = config
                    processed_tags.add(tag)
                    new_tags_added = True

            if not new_tags_added:
                break
        result: List[TagMatch] = [
            x for x in self.tag_match_list if x.tag in tag_configs
        ]
        return result

    def match_content(
        self, content: str, tag_range: List[str] = []
    ) -> List[MatchResult]:

        match_results: List[MatchResult] = []
        if content:
            content = content.lower().strip()
            content_len = len(content)
            # 需要copy, 因为tag_list会改变
            tag_list = (
                self.get_tag_range(tag_range)
                if tag_range
                else self.tag_match_list.copy()
            )

            for x in tag_list:
                # 仅当content 长度大于tag+ifx长度时才有可能匹配到
                if content_len < x.match_length:
                    continue
                # 简单匹配
                matched = None
                # add content's space for EN tag match
                content_for_match = f" {content} " if x.language == "EN" else content
                # 不论是否有pattern,先简单匹配
                # if not x.pattern:
                matched = x.basic_match if x.basic_match in content_for_match else None
                # 仅当简单匹配没有匹配到时才进行正则匹配
                # else:
                if not matched and x.pattern:
                    re_match = re.search(x.pattern, content_for_match)
                    matched = re_match.group() if re_match else None
                if matched:
                    match_results.append(
                        MatchResult(
                            x.prefix,
                            x.suffix,
                            x.tag,
                            x.category,
                            x.data_phase,
                            x.data_cycle,
                            matched.strip(),
                        )
                    )
                    # 如果匹配到，则去除后续的父标签及无前缀、后缀标签
                    if x.prefix or x.suffix:
                        for t in reversed(tag_list[tag_list.index(x) + 1 :]):
                            if t.prefix is None and t.suffix is None and t.tag == x.tag:
                                tag_list.remove(t)
                    if x.parent_tags and len(x.parent_tags):
                        for p_tag in x.parent_tags:
                            for t in reversed(tag_list[tag_list.index(x) + 1 :]):
                                if (
                                    t.prefix is None
                                    and t.suffix is None
                                    and t.tag == p_tag
                                ):
                                    tag_list.remove(t)
        return match_results

    def match_result(
        self,
        content: str,
        return_type: int = 0,
        tag_range: List[str] = [],
        tag_verion="DEV",
        udf_version="DEV",
    ) -> List[str]:
        match_results = self.match_content(content, tag_range)
        # for debug use
        if return_type == -1:
            tag_list = (
                self.get_tag_range(tag_range)
                if tag_range
                else self.tag_match_list.copy()
            )
            return [
                "{}_{}_{}_{}.{}".format(
                    x.tag,
                    x.prefix,
                    x.suffix,
                    tag_verion,
                    udf_version,
                )
                for x in tag_list
            ]
        return_results = []
        for r in match_results:
            if return_type == 0:
                formated_result = "{}_{}_{}_{}_{}_{}.{}".format(
                    r.matched,
                    r.tag,
                    r.category,
                    r.data_phase,
                    r.data_cycle,
                    tag_verion,
                    udf_version,
                )
            elif return_type == 1:  # 标志出prefix和tag匹配结果
                formated_result = r.matched
            elif return_type == 2:  # 输出匹配的纯文本
                formated_result = r.tag
            # return category only
            elif return_type == 3:
                formated_result = r.category
            # return data_phase only
            elif return_type == 4:
                formated_result = r.data_phase
            # return category & data cycle
            elif return_type == 5:
                formated_result = "{}_{}_{}".format(
                    r.category, r.data_phase, r.data_cycle
                )
            else:
                formated_result = r.tag
            return_results.append(formated_result)
        counter_results = Counter(return_results)
        return (
            [
                "{}@{}".format(element, count)
                for element, count in counter_results.items()
            ]
            if return_type > 1
            else return_results
        )
