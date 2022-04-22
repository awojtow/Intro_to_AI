from data import Data
from estimator import ID3
from sklearn import metrics
import numpy as np
from eval_metrics import *
import os
from consts import *
from kfold import kfold
import matplotlib.pyplot as plt
import pandas as pd


def build_example_tree(data):
        train, test = data.split(0.01)
        tree = ID3()
        tree.fit(train)
        tree.draw_tree()
      

def do_kfold(nfold,data):
        kfold(nfold, data, imbalanced = True)

def plot_analise_kfold(df_dict_test):
        for name in CLASS_NAMES:
                plt.figure()
                x = df_dict_test[name].index.tolist()
                x = [100 - 100/x for x in x]
                measure_colors = ['red','blue', 'green', 'orange']
                i = 0
                for measure in SCORE_TYPES:
                        color = measure_colors[i]
                        i+=1
                        plt.plot(x, df_dict_test[name][measure],color = color, label = measure + '_test')
                plt.title(f'Measures for class {name}')
                plt.xlabel('% of data used to train')
                plt.ylabel("Mean fold measure value")
                plt.legend()
                plt.savefig(f"k_measures_class_{name}")


def analise_kfold(kfold_list):
        df_dict = {}
        for clas in CLASS_NAMES:
                df_dict[clas] = pd.DataFrame(columns = SCORE_TYPES, index = kfold_list)
        for fold in kfold_list:
                result = pd.read_csv(os.getcwd()+f'/kfold_scores_k_{fold}__test.csv')
                for clas in CLASS_NAMES:
                        df_dict[clas].loc[fold] = pd.DataFrame(result.loc[result['class'] == clas])[SCORE_TYPES].values


        plot_analise_kfold(df_dict)

        # return df_dict

def train_and_test_example(data):
        train, test = data.split(0.8)
        model = ID3()
        model.fit(train)
        pred = model.predict_dataset(test)
        real = test.y
        confussion_matrix(y_pred = pred, y_real = real, save = True)
        caluculate_measures(y_pred =pred, y_real = real, name ='example',save = True)

def train_all(data):
        model = ID3()
        model.fit(data)
        pred = model.predict_dataset(data)
        real = data.y
        confussion_matrix(y_pred = pred, y_real = real, save = True, name = 'all')
        caluculate_measures(y_pred =pred, y_real = real, name ='all',save = True)
def main():
        dirname = 'results2'
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, dirname)
        # os.mkdir(path)
        os.chdir(path)

        data = Data(path = PATH, att_names = ATT_NAMES, clas_name = CLASS_NAME)
        data.data_analisis()

        # build_example_tree(data)
        # train_and_test_example(data)
        
        # for i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
        #         do_kfold(i, data)

        # analise_kfold( [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        train_all(data)
   
if __name__=="__main__":
    main()
