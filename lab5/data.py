import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
def fetch_data(path = "/Users/agnieszkawojtowicz/Documents/POLI/SEM2/WSI/cw5/dataset/mnist_784.csv"):
    data= pd.read_csv(path)
    return data

def split_data(dataset):
    data = dataset.copy()
    Y = data.pop("class")
    X_train, X_test, y_train, y_test = train_test_split(data, Y,  train_size = 0.8)
    return X_train, X_test, y_train, y_test

def visualise_example(x,y_real, y_pred, name = ''):
    x =  x.reshape((28, 28)) * 255
    fig = plt.figure()
    plt.imshow(x, cmap='gray')
    plt.title(f"Example class {y_real}, prediction {y_pred}")
    plt.savefig(f"example_p_{y_pred}_r_{y_real}_"+name)


def hist_data(data):
    y = data.pop("class")
    fig = plt.figure()
    plt.hist(y, bins = 10)
    plt.xlabel('Class value')
    plt.ylabel('Class example number')
    plt.title(f"Histogram of class values")
    plt.savefig(f"clas_histogram")

