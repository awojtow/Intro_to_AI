
import anytree
from anytree.exporter import DotExporter

def nodenamefunc(node):
    return '%s' % (node.name)
def edgeattrfunc(node, child):
    #   return 'label="%s:%s"' % (node.name, child.name)
    return 'label="%s"' % (child.weight)
    # return child.weight
    # return 10
def edgetypefunc(node, child):
   return '--'

class Node:
    def __init__(self):
        self.subnodes = {}
        self.split_criteria = ""
        self.gain = 0
        self.leaf = False
        self.clas = ""
        self.dominant_class = ""
        self.__global_idx = 0



    def __display_subtree(self, parent_node, parent_node_tree):
        self.__global_idx+=1
        if parent_node.leaf:
            return
        for key, child in parent_node.subnodes.items():
            self.__global_idx+=1
            # name = f"key:{key} split: {child.split_criteria}" if not child.leaf else f"key:{key} class:{child.clas}"
            name = f"sp: {child.split_criteria} {self.__global_idx}" if not child.leaf else f"cl:{child.clas} {self.__global_idx}"
            child_tree = anytree.Node(name, parent = parent_node_tree, weight = key)
            self.__display_subtree(child, child_tree)
        
    def display(self):
        name = f"sp: {self.split_criteria}:" if not self.leaf else f"cl: {self.clas}:"
        tree_root = anytree.Node(name, parent=None, edge = 1)
        self.__display_subtree(self, tree_root)
        DotExporter(tree_root,graph="graph",nodenamefunc=nodenamefunc,
                    nodeattrfunc=lambda node: "shape=box",
                    edgeattrfunc=edgeattrfunc,
                    edgetypefunc=edgetypefunc).to_picture(f"id3_tree.png")

