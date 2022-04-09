
import anytree
from anytree.exporter import DotExporter

class Node:
    def __init__(self, board, move = None, depth = 0):
        self.board = board
        self.move = move
        self.score = None
        self.children = []
        self.depth = depth
        self.winning = False
        self.terminal = False
        self.global_idx = 0
    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_depth(self, depth):
        self.depth = depth

    def append_child(self, child):
        self.children.append(child)


    def __draw_subtree(self, parent_node, parent_node_tree):
        self.global_idx+=1
        if parent_node.terminal or parent_node.depth == 0 or parent_node.winning:
            return
        for child in parent_node.children:
            self.global_idx+=1
            name = f"m:{child.move} ps: {child.score}  id: {self.global_idx}:"
            child_tree = anytree.Node(name, parent = parent_node_tree)
            self.__draw_subtree(child, child_tree)
        
    def draw_tree(self, move_idx):
        name = f"ps: {self.score}:"
        tree_root = anytree.Node(name)
        self.__draw_subtree(self, tree_root)

        DotExporter(tree_root).to_picture(f"game_tree_{move_idx}.png")


