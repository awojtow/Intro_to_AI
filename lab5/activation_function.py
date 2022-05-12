
import numpy as np

def sigmoid(vec_x):
    return 1 / (1 + np.exp(-vec_x))

def softmax(vec_x):
    #vec_x = vec_x - np.max(vec_x, axis = 1, keepdims = True) #protect from overflow
    return np.exp(vec_x) / np.sum(np.exp(vec_x), axis=0)


def sigmoid_der(vec_x):
    f = 1/(1+np.exp(-vec_x))
    return f * (1 - f)

def fun(vec_x):
    return vec_x

def fun_der(vec_x = None):
    return 1