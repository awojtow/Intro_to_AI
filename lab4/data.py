import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from consts import *
import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))


class Data:
    def __init__(self, clas_name, path = "", att_names = None, data = pd.DataFrame()):
        if path != "":
            self.df = pd.read_csv(names = att_names + [clas_name], filepath_or_buffer = path)
            self.clas_name = clas_name
        elif not data.empty:
            self.df = data
            self.clas_name = clas_name
        else:
            print('no data supplied implement error')
        self.y = self.df[clas_name]
        self.X = self.df.drop(clas_name, axis = 1)

    def split(self,rate):
        train_df = self.df.sample(frac = rate)
        test_df = self.df.drop(train_df.index)
        train_data = Data(clas_name = self.clas_name, data = train_df)
        test_data = Data(clas_name = self.clas_name, data = test_df)
        return train_data, test_data

    def sort(self):
        self.df = self.df.sort_values(by = list(self.df.columns))
        self.y = self.df[self.clas_name]
        self.X = self.df.drop(self.clas_name, axis = 1)

    def __attribute_data_analisys(self,att, norm = True):

        subdf = self.df[[self.clas_name,att]].value_counts()
        clas_name = pd.unique(self.y)
        clas_counts = pd.value_counts(self.y)

        att_result = pd.DataFrame()
        for name in clas_name:
            result = subdf.loc[name].div(clas_counts.loc[name]) if norm else subdf.loc[name]
            att_result = pd.concat([att_result, result], axis = 1)
        att_result.columns = list(clas_name)

        return att_result
    
    def __plot_compare_data_analisys(self, att_result_norm, att_result, att_name):
        fig = plt.figure()
        ax0 = fig.add_subplot(1,2,1)
        ax0 = att_result_norm.plot.bar(ax = ax0)
        ax0.set_title("Fraction of attribute values in classes", size = 9)
        ax0.set_xlabel("Attribute value")
        ax0.set_ylabel("Num of instances in class with value \n/Num of instances in class", size = 9) 

        ax1 = fig.add_subplot(1,2,2)
        ax1 = att_result.plot.bar(ax = ax1)
        ax1.set_title("Number of attribute values in classes", size = 9)
        ax1.set_xlabel("Attribute value")
        ax1.set_ylabel("Num of instances in class with value", size = 9) 

        fig.suptitle(f"Attribute \"{att_name}\" distribution")
        fig.tight_layout()
        fig.savefig(f"hist_{att_name}_compare")



    def data_analisis(self):
        for att in ATT_NAMES:
            result_norm = self.__attribute_data_analisys(att)
            result = self.__attribute_data_analisys(att, norm = False)
            self.__plot_compare_data_analisys(result_norm, result, att)
