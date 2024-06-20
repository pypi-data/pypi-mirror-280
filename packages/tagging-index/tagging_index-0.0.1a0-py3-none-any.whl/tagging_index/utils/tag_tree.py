from typing import List, Optional
from treelib import Node, Tree
from tagging_index._udf.tag_converter import TagConfig


class TagNode(Node):
    def __init__(
        self, tag=None, identifier=None, expanded=True, data: Optional[TagConfig] = None
    ):
        super().__init__(tag, identifier, expanded, data)
        self.level = data.tag_level if data else 0


class TagTree(Tree):

    def __init__(
        self,
        tag_configs: List[TagConfig],
    ):
        super().__init__(node_class=TagNode)
        tag_configs.sort(key=lambda x: x.tag_level)
        self.tag_configs = tag_configs
        if tag_configs:
            root_tag = self.create_node("**tag_root**")
            invalid_parent = self.create_node("**invalid_parent**", parent=root_tag)
            for c in tag_configs:
                p = c.parent_tags[0] if c.parent_tags else root_tag.identifier
                if self.contains(p):
                    self.create_node(c.tag, c.tag, parent=p, data=c)
                else:
                    invalid_p = self.create_node(p, p, parent=invalid_parent)
                    self.create_node(c.tag, c.tag, parent=invalid_p, data=c)
            # remove invalid tag if no child
            invalid_count = len(self.children(invalid_parent.identifier))
            if invalid_count == 0:
                self.remove_node(invalid_parent.identifier)

    def show_level(self, nid=None, levels=0):
        """print tree from nid to below levels, default levels = 0 to print all level below nid

        Args:
            levels (int, optional): how may levels under nid to print. Defaults to 0.
        """
        node = self.get_node(nid)
        if node:
            level = node.level + levels
            path = [x for x in self.rsearch(nid)]
            children = self.children(node.identifier)
            all_node = path + [
                x.identifier for x in children if x.level <= level or levels == 0
            ]
            print(self.show(filter=lambda x: x.identifier in all_node, stdout=False))
        else:
            level = levels
            print(
                self.show(
                    nid=nid,
                    filter=lambda x: (x.level <= level) or levels == 0,
                    stdout=False,
                )
            )
