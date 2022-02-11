from dataAnalysis.RDA import *
import pandas as pd
from sklearn.model_selection import train_test_split
from dataAnalysis.svm_model import *
from dataAnalysis.feature_selection import *
from dataAnalysis.dataset import load_data, Data_miRna

#file1 = "bh.txt"
#file2 = "us.txt"

def select(file1, file2):
    """file1:正常人数据 file2:病人数据"""
    data_new = load_data(file1, file2)

    y_new = Data_miRna.getY(data_new)

    max_mix_score, max_accuracy, max_f1, best_report, \
    best_params, best_w, best_b, combine = featSelect(data_new, y_new)

    # return max_mix_score, max_accuracy, max_f1, best_report, best_params, best_w, best_b, combine
    return combine, best_w

# combine, w = select(file1, file2)

# print(combine)
# print(w)
