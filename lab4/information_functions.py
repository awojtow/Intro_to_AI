from node import Node
import numpy as np
def information(data, clas_name):
    information = 0
    for clas in data[clas_name].unique():
        frac= data[clas_name].value_counts()[clas]/len(data)
        information += -frac*np.log2(frac)
    return information

def entrophy(data, attribute, clas_name):
    entrophy = 0
    for value in data[attribute].unique():
        subdata = data[data[attribute]==value]
        entrophy += len(subdata)/len(data) * information(subdata, clas_name)
    return entrophy

def info_gain(data, attribute, clas_name):
    return information(data, clas_name) - entrophy(data, attribute, clas_name)
    
def max_gain_attribute(data, clas_name):
    attributes = data.drop(clas_name,1).columns
    name, max_gain = attributes[0], info_gain(data, attributes[0], clas_name)
    for att in attributes[1:]:
        if info_gain(data, att, clas_name) > max_gain:
            name = att
            max_gain = info_gain(data, att, clas_name)
    return name, max_gain