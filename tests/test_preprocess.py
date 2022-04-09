from src import preprocess as pp
import pandas as pd



df1 = pd.DataFrame(
    {"Student": [101, 102, 103, 104, 105], "Grades": [100, 80, 75, 95, 97]}
)


df2 = pd.DataFrame(
    {"Student": [101, 102, 103, 104, 105, 106], "Grades": [100, 80, 75, 95, None, 90]}
)


df3 = pd.DataFrame(
    {"Student": [101, 102, 103, 104, 105, 106], "Grades": [100, 80, 75, 95, 86, 90]}
)



def test_preprocess_perfect():
    # check if the function properly split the dataframe to train and test 
    trainset_a, testset_a = pp.preprocess(df1, 0.8, 20)
    assert len(trainset_a.index) == 4
    assert len(testset_a.index) == 1


def test_preprocess_with_missing_value():
    # check if the function properly removes null values
    trainset_b, testset_b = pp.preprocess(df2, 0.8, 20)
    assert len(trainset_b.index) == 4
    assert len(testset_b.index) == 1


def test_preprocess_2_fold():
    # check if the function properly split the dataframe to train and test by 50%/50%
    trainset_c, testset_c = pp.preprocess(df3, 0.5, 20)
    assert len(trainset_c.index) == 3
    assert len(testset_c.index) == 3
