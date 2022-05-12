from regex import R
from layer import *

#activations iterate forward
#backwards has to have loss (ouptut - real_output) as first element, iterate backwards

import logging
import sys
from helper import *

class Network():
    def __init__(self):
        self.layers = []
    
    def add_layer(self, layer):
        self.layers.append(layer)


    def set_layers(self, layers):
        self.layers = layers


    def forward(self, input):
        self.layers[0].forward_layer(input)
        for l_i in range(1, len(self.layers)):
            self.layers[l_i].forward_layer(self.layers[l_i - 1].get_forward_act())
        return self.layers[-1].get_forward_act()


    def get_loss(self, output, real_output):
        return output - real_output

    def backward(self, loss):
        self.layers[-1].set_backward(loss)
        i = len(self.layers) - 2
        while i >=0:
            self.layers[i].backward_layer(self.layers[i+1].get_backward(), self.layers[i+1].get_weights())
            i-=1


    
    def update_params(self, alpha, input):
        self.layers[0].update_layer_params(alpha, input)
        for l_i in range(1, len(self.layers)):            
            self.layers[l_i].update_layer_params(alpha, self.layers[l_i - 1].get_forward_act())

        
    def do_gradient_descent(self, input, real_output, alpha):
        last_layer_act = self.forward(input)
        loss = self.get_loss(last_layer_act, real_output)
        self.backward(loss)
        self.update_params(alpha, input)
        return decode_label(last_layer_act)

    def predict_one(self, input):
        last_layer_act = self.forward(input)
        return decode_label(last_layer_act)

    def predict_batch(self, x_data, y_data):
        real_x = np.array(x_data)
        real_y = np.array(y_data)
        predicted = np.zeros(real_x.shape[0])
        for i in range(real_x.shape[0]):
            predicted[i] = self.predict_one(real_x[i])
        accuracy = get_accuracy(pred = predicted, real = real_y)
        return accuracy

    def fit_batch(self, x_data, y_data, alpha):
        predicted = np.zeros(len(y_data))
        real_y = np.array(y_data)
        real_x = np.array(x_data)
        for i in range(len(y_data)-1):
            y = real_y[i]
            x = real_x[i]
            predicted[i] = self.do_gradient_descent(x, hot_encode_label(y), alpha)  
        accuracy = get_accuracy(pred = predicted, real = real_y)
        return accuracy 
        # logging.info(f"Accuracy: {accuracy}")

    
    


