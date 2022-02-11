from dataAnalysis.RDA import *
import pandas as pd
from sklearn.model_selection import train_test_split
from dataAnalysis.svm_model import *
from dataAnalysis.feature_selection import *
from dataAnalysis.dataset import load_data, Data_miRna

import warnings

warnings.filterwarnings("ignore")

#file1 = "bh.txt"
#file2 = "us.txt"

def select(file1, file2):
    """file1:正常人数据 file2:病人数据"""
    data_new = load_data(file1, file2)

    # 检验是否存在空值
    T1 = data_new.bh.isnull().any().any()
    T2 = data_new.us.isnull().any().any()
    if T1 or T2:
        return [[0], "There is a NAN value in the data"]

    y_new = Data_miRna.getY(data_new)

    max_mix_score, max_accuracy, max_f1, best_report, \
    best_params, best_w, best_b, combine = featSelect(data_new, y_new)

    result = [best_w[0].tolist(), combine]

    return result

    # return max_mix_score, max_accuracy, max_f1, best_report, best_params, best_w, best_b, combine
    return combine, best_w

# combine, w = select(file1, file2)

# print(combine)
# print(w)
