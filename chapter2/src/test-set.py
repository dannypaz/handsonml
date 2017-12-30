import os
import pandas as pd
import numpy as np

HOUSING_PATH = "datasets/housing"
HOUSING_FILE = "housing.csv"

def load_housing_data(housing_path=HOUSING_PATH, housing_file=HOUSING_FILE):
    """ Loads housing csv data """
    csv_path = os.path.join(housing_path, housing_file)
    return pd.read_csv(csv_path)

def split_train_test(data=load_housing_data(), test_ratio=0.2):
    """ Splits our data into train and test files """
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

split_train_test()
