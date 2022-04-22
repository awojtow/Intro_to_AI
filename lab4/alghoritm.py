from node import Node
from information_functions import max_gain_attribute
def ID3_alghoritm(data, parent_data, clas_name):
    # max_depth = len(data.columns) - 1
    node = Node()
    if len(data) == 0:    
        node.leaf = True
        # node.split_criteria = "class: "
        node.clas = parent_data[clas_name].value_counts().idxmax()
        return node
    elif len(data.columns) == 1 or data[clas_name].nunique() == 1:
        node.leaf = True
        # node.split_criteria = 
        node.clas = data[clas_name].value_counts().idxmax()
        return node
    else: 
        max_criteria, max_gain = max_gain_attribute(data, clas_name)
        node.split_criteria, node.gain = max_criteria, max_gain
        node.dominant_class = data[clas_name].value_counts().idxmax()
        for value in data[node.split_criteria].unique():
            subdata = data[data[node.split_criteria] == value].drop(node.split_criteria,1)
            subnode = ID3_alghoritm(subdata, data, clas_name)
            node.subnodes[str(value)] = subnode
        return node
