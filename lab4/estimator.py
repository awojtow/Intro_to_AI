from node import Node
from alghoritm import ID3_alghoritm
from data import Data
class ID3:
    def __init__(self):
        self.root_node = None

    def fit(self,data):
        self.root_node = ID3_alghoritm(data.df, data.df, data.clas_name)
        
    def __predict_example(self, node, example):
        if node.leaf:
            return str(node.clas)
        else:
            if str(example[(node.split_criteria)]) in node.subnodes.keys():
                next_node = node.subnodes[str(example[(node.split_criteria)])]
                return self.__predict_example(next_node, example.drop(node.split_criteria))  
            else:
                return node.dominant_class
    def predict_example(self, example):
        return self.__predict_example(self.root_node, example)  
    
    def predict_dataset(self,dataset):
        return [self.predict_example(dataset.df.iloc[i]) for i in range(len(dataset.df))]

    def draw_tree(self):
        self.root_node.display()