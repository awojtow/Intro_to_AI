
import matplotlib.pyplot as plt
from layer import Layer
from helper import *
from activation_function import *
from network import Network
import pandas as pd
from data import *
from helper import *

import logging
import sys
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', 
                    level=logging.INFO, 
                    filename = 'log.txt')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))




def get_two_layer_network(hidden_neurons = 10):
    size = (hidden_neurons,784)
    size2 = (10, hidden_neurons)
    layer0 = Layer(size = size, activation_function=sigmoid, activation_der=sigmoid_der, name = 'pierwsza wagowa')
    layer1 = Layer(size = size2, activation_function=softmax,  name = 'druga wagowa')
    nn = Network()
    nn.set_layers([layer0, layer1])
    return nn

def get_multilayer_network(num_of_layers = 3, hidden_neurons = 10):
    size_beg = (hidden_neurons,784)
    size_end = (10, hidden_neurons)
    layer_beg = Layer(size = size_beg, activation_function=sigmoid, activation_der=sigmoid_der, name = 'pierwsza wagowa')
    layer_end = Layer(size = size_end, activation_function=softmax,  name = 'druga wagowa')
    layers = [layer_beg]
    for i in range(num_of_layers - 2):
        layer_i =  Layer(size = (hidden_neurons, hidden_neurons), activation_function=sigmoid, activation_der=sigmoid_der, name = f"{i} -ta wagowa")
        layers.append(layer_i)
    layers.append(layer_end)
    nn = Network()
    nn.set_layers(layers=layers)
    return nn

def plot_accuracy(train_accuracy, test_accuracy, name = ""):
    epochs = [i for i in range(len(train_accuracy))]
    plt.figure()
    plt.plot(epochs, train_accuracy, label = 'train', c = 'blue')
    plt.plot(epochs, test_accuracy, label = 'test', c = 'red')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of test and training data")
    plt.legend()
    plt.savefig(f"accuracy_{name}.png")

def get_few_examples(data):
    epochs_count = 80
    learning_rate = 0.01
    nn = get_two_layer_network(hidden_neurons = 20)
    X_train, X_test, y_train, y_test = split_data(data)
    X_train, X_test, y_train, y_test = np.array(X_train), np.array(X_test), np.array(y_train), np.array(y_test)
    for e in range(epochs_count):
        train_acc = nn.fit_batch(X_train, y_train, alpha = learning_rate)
    
    print(f"Last train acc is {train_acc}")
    good_limit = 3
    bad_limit = 3
   
    while good_limit > 0 or bad_limit > 0:
        random_idx = np.random.randint(low = 0, high = len(y_test)-1)
        randomX, randomY = X_test[random_idx], y_test[random_idx]
        X_test = np.delete(X_test, random_idx, axis = 0)
        y_test = np.delete(y_test, random_idx, axis = 0)
        pred = nn.predict_one(randomX)
        if pred == randomY:
            visualise_example(randomX, y_real = randomY, y_pred = pred)
            good_limit -=1
        elif pred != randomY:
            visualise_example(randomX, y_real = randomY, y_pred = pred)
            bad_limit -=1




def train_test_network(nn, data, epochs_count, learning_rate, name):
    X_train, X_test, y_train, y_test = split_data(data)
    train_accuracy = []
    test_accuracy = []
    for e in range(epochs_count):
        train_acc = nn.fit_batch(X_train, y_train, alpha = learning_rate)
        test_acc = nn.predict_batch(X_test, y_test)
        train_accuracy.append(train_acc)
        test_accuracy.append(test_acc)
        print(f"epoch {e}, train_acc {train_acc}, test_acc {test_acc}")
    plot_accuracy(train_accuracy, test_accuracy, name)


def main():
    data = fetch_data()
    epochs_count = 80
    # for hidden_neuron in [5,10,30,100]:
    #     nn = get_two_layer_network(hidden_neurons = hidden_neuron)
    #     train_test_network(nn, data, epochs_count, learning_rate=0.01, name = f"n_neur_{hidden_neuron}")

    
    # for learning_rate in [1, 0.5, 0.1, 0.01, 0.001]:
    #     nn = get_two_layer_network(hidden_neurons = 20)
    #     train_test_network(nn, data, epochs_count, learning_rate=learning_rate, name = f"lr_{learning_rate}")


    # for hidden_layer_num in [0,1,3,5]:
    #     nn = get_multilayer_network(num_of_layers = hidden_layer_num, hidden_neurons=20)
    #     train_test_network(nn, data, epochs_count, learning_rate=0.01, name = f"layers_{hidden_layer_num}")
    
    
    get_few_examples(data)
    # hist_data(data)

    
        

if __name__ == '__main__':
    main()