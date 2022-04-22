from sklearn.model_selection import KFold 
from eval_metrics import caluculate_measures
from data import Data
from estimator import ID3
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from consts import *

def kfold(n_splits, data,imbalanced = False, name = ''):
    score_types = SCORE_TYPES
    score_measures_test = pd.DataFrame(columns = ['class'] + score_types, index = [0,1,2,3], data = np.zeros((4,5)))
    score_measures_test['class'] = CLASS_NAMES
    
    score_measures_train = pd.DataFrame(columns = ['class'] + score_types, index = [0,1,2,3], data = np.zeros((4,5)))
    score_measures_train['class'] = CLASS_NAMES
    if imbalanced:
        kf = StratifiedKFold(n_splits=n_splits, random_state=RANDOM_STATE, shuffle=True)
        iterate = kf.split(data.X, data.y)
    else:
        kf = KFold(n_splits=n_splits, random_state=RANDOM_STATE, shuffle=True)
        iterate = kf.split(data.X)

    for train_index, test_index in iterate:
        train_index = list(train_index)
        test_index = list(test_index)
        train = data.df.loc[train_index]
        test = data.df.loc[test_index]

        train_data = Data(clas_name = data.clas_name, data = train)
        test_data = Data(clas_name = data.clas_name,data = test)
        model = ID3()
        model.fit(train_data)

        pred_test = model.predict_dataset(test_data)
        real_test = test_data.y
        
        measures_test = caluculate_measures(pred_test, real_test, save = False, name = 'n')
        measures_test =(pd.DataFrame({'class':CLASS_NAMES}).merge(measures_test, on='class'))
        score_measures_test[score_types] = score_measures_test[score_types].values + measures_test[score_types].values
        
    
    score_measures_test[score_types] = score_measures_test[score_types].values/n_splits
   
    score_measures_test.to_csv(f'kfold_scores_k_{n_splits}_{name}_test.csv')

    
           

