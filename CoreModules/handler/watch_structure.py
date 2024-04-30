import maya.cmds as cmds
import os
import yaml

from pprint import pprint

class WatchGroupStructure(object):

    def __init__(self, root_node=None, file_path=None, file_name=None):

        self.root_node = root_node
        self.file_path = file_path
        self.file_name = file_name
        self.node_structure = None
        self.hierarchy_result = None

    def trace_group_structure(self):
        def get_group_hierarchy(node, hierarchy=None):
            if hierarchy is None:
                hierarchy = dict()

            hierarchy[node] = list()

            children = cmds.listRelatives(node, children=True, fullPath=True) or []

            if not children:
                return hierarchy

            for child in children:
                hierarchy[node].append(get_group_hierarchy(child))

            return hierarchy

        def show_hierarchy(top_node, parent_root=False):

            line_text = list()

            for key, values in top_node.items():

                node_type = cmds.nodeType(key)

                if not parent_root:

                    text = f"{key}, {node_type}"
                    # line_text.append((text, key))
                    line_text.append(key)
                else:
                    parent_level = len(key.split('|')) - 1
                    text = f"{parent_level * '|'} {key.rsplit('|', 1)[-1]}, {node_type}"
                    # line_text.append((text, key))
                    line_text.append(key)
                for obj in values:
                    line_text.extend(show_hierarchy(obj, parent_root=True))
            return line_text

        self.hierarchy_result = get_group_hierarchy(self.root_node)
        self.node_structure = show_hierarchy(self.hierarchy_result)



    def main(self):
        self.trace_group_structure()

        if not os.path.isdir(self.file_path):
            os.makedirs(self.file_path)

        with open(os.path.join(self.file_path, self.file_name), 'w') as f:
            yaml.dump(self.node_structure, f)






