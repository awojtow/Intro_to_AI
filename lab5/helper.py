import numpy as np
def init_weights(size):
    return np.random.rand(size[0], size[1]) - 0.5

def init_bias(size):
    return np.random.rand(size[0]) - 0.5

def hot_encode_label(label, num_classes = 10):
    label_o = np.zeros((num_classes))
    label_o[label] = 1
    return label_o
    
def decode_label(hot_enc_label):
    return np.argmax(hot_enc_label)

def get_accuracy(pred, real):
    return np.sum((pred == real))/len(pred)



