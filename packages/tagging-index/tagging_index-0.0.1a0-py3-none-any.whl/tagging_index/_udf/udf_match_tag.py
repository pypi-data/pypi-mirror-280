from odps.udf import annotate


# UDF类
@annotate("string,bigint,array<string>->array<string>")
class match_tag(object):
    def __init__(self):
        import sys

        deps = ["tag_matcher.py", "tag_converter.py"]
        for dep in deps:
            sys.path.insert(0, f"work/{dep}")
        from tag_matcher import TagMatcher
        from tag_converter import TagConverter

        self.converter = TagConverter()
        self.tag_version, self.tag_configs = self.converter.udf_res_to_config(
            "res_dim_tag_new"
        )
        self.matcher = TagMatcher()
        self.matcher.load_tags(self.tag_configs)

    def evaluate(self, content, return_type, tag_range):
        # !UDF_VERSION 会在dataworks 上发布时自动添加
        match_results = self.matcher.match_result(content, return_type, tag_range, self.tag_version, UDF_VERSION)  # type: ignore
        return match_results
