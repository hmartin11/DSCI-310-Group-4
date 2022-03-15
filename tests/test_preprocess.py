from src import preprocess as pp
import pandas as pd
import pytest


df1 = pd.DataFrame({'Student': [101, 102, 103, 104, 105], 'Grades': [100, 80, 75, 95, 97]})
df1_train_result = pd.DataFrame({'Student': [101, 102, 103, 104], 'Grades': [100, 80, 75, 95]})
df1_test_result = pd.DataFrame({'Student': [105], 'Grades': [97]})

df2 = pd.DataFrame({'Student': [101, 102, 103, 104, 105, 106], 'Grades': [100, 80, 75, 95, None, 90]})
df2_train_result = df1_train_result = pd.DataFrame({'Student': [101, 102, 103, 104], 'Grades': [100, 80, 75, 95]})
df2_test_result = pd.DataFrame({'Student': [106], 'Grades': [90]})

df3 = pd.DataFrame({'Student': [101, 102, 103, 104, 105, 106], 'Grades': [100, 80, 75, 95, 86, 90]})
df3_train_result = df1_train_result = pd.DataFrame({'Student': [101, 102, 103], 'Grades': [100, 80, 75]})
df3_test_result = pd.DataFrame({'Student': [104, 105, 106], 'Grades': [95, 86, 90]})


def test_preprocess_perfect():
    trainset_a, testset_a = pp.preprocess(df1, 0.8, 20)
    assert len(trainset_a.index) == 4
    assert len(testset_a.index) == 1
    
def test_preprocess_with_missing_value():
    trainset_b, testset_b = pp.preprocess(df2, 0.8, 20)
    assert len(trainset_b.index) == 4
    assert len(testset_b.index) == 1

def test_preprocess_2_fold():
    trainset_c, testset_c = pp.preprocess(df3, 0.5, 20)
    assert len(trainset_c.index) == 3
    assert len(testset_c.index) == 3
