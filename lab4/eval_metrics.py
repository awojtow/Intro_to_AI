import matplotlib
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np 

def multiclass_to_binary_cm(cm, clas):
    TP = cm.loc[clas,clas]
    FP = cm.loc[clas,:].sum() - TP
    FN = cm.loc[:,clas].sum() - TP
    TN = cm.sum().sum() - (TP + FP + FN )
    return TP, FP, TN, FN

def precision(TP, FP, TN, FN):
    return round(TP/(TP+FP),2)

def accuracy(TP, FP, TN, FN):
    return round((TP + TN)/(TP + FP + TN + FN),2)

def recall(TP, FP, TN, FN):
    return round(TP/(TP+FN),2)

def f1score(TP, FP, TN, FN):
    return round(2*precision(TP, FP, TN, FN) * recall(TP, FP, TN, FN)/(precision(TP, FP, TN, FN) + recall(TP, FP, TN, FN)),2)

def confussion_matrix(y_pred, y_real, save = True, name = ""):
    results = pd.DataFrame({'pred':y_pred, 'real':y_real})
    conf = pd.crosstab(results.pred, results.real)
    if save:
        plt.figure()
        sb.heatmap(conf,annot = True, cmap = 'Blues')
        plt.savefig(f'confusion_matrix_{name}')
    return conf

def caluculate_measures(y_pred, y_real, name, save = False):
    confusion_matrix = confussion_matrix(y_pred, y_real, save = False)
    found_classes = np.unique(y_real)
    measures = pd.DataFrame(columns = ['class','precision', 'recall', 'accuracy', 'f1-score'])
    for clas in found_classes:
        TP, FP, TN, FN = multiclass_to_binary_cm(confusion_matrix, clas)
        class_df = {'class':clas,'precision':precision(TP, FP, TN, FN),
                                 'recall':recall(TP, FP, TN, FN),
                                 'accuracy':accuracy(TP, FP, TN, FN), 
                                 'f1-score':f1score(TP, FP, TN, FN)}
        measures = measures.append(class_df, ignore_index= True)
    if save:
        measures.to_csv(f'measures_{name}.csv')
    return measures


