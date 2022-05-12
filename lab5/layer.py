import numpy as np
from helper import *
from activation_function import *

class Layer():
    def __init__(self, size, activation_function = fun, activation_der = fun_der, name = ""):
        self.size = size
        self.weights = init_weights(size)
        self.bias = init_bias(size)
        self.act_function = activation_function
        self.activation_der = activation_der
        self.name = name
        self.__forward = None
        self.__forward_act = None
        self.__backward = None

    def set_forward(self, forward):
        self.__forward = forward
    
    def set_forward_act(self, forward):
        self.__forward_act = forward

    def set_backward(self, backward):
        self.__backward = backward 

    def get_forward(self):
        return self.__forward
    
    def get_forward_act(self):
        return self.__forward_act

    def get_backward(self):
        return self.__backward

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def set_bias(self, bias):
        self.bias = bias
        
    def forward_layer(self, input):
        output = self.weights.dot(input) 
        output += self.bias
        self.__forward = output
        self.__forward_act = self.act_function(output)
      
    def backward_layer(self, upper_d, upper_w):
        self.__backward =  np.dot(upper_w.T, upper_d) * self.activation_der(self.__forward)

    def update_layer_params(self, alpha, lower_forward_act):
        sb = self.__backward.reshape(-1,1)
        lf = lower_forward_act.reshape(-1,1)
        dw = 1/self.size[0] * alpha * np.dot(sb, lf.T)
        db = 1/self.size[0] * alpha * sb[:,0]
        self.update_weights(dw)
        self.update_bias(db) 

    def update_weights(self, update):
        self.weights = self.weights - update

    def update_bias(self, update):
        self.bias = self.bias - update
        
    def __str__(self):
        return f"name {self.name}\
                weight size {self.size}\
                act size {self.__forward_act.shape}\
                backward size {self.__backward.shape}"

