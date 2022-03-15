from src import preprocess as pre
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
    output1, output2 = pre.preprocess(df1, 0.8)
    pd.testing.assert_frame_equal(output1,df1_train_result)
    pd.testing.assert_frame_equal(output2,df1_test_result)

    # assert output1 == df1_train_result
    # assert output2 == df1_test_result
    
def test_preprocess_with_missing_value():
    assert pre.preprocess(df2, 0.8) == df2_train_result, df2_test_result

def test_preprocess_2_fold():
    assert pre.preprocess(df3, 0.5) == df3_train_result, df3_test_result
    
    