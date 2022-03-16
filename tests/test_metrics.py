from src import metrics_function
import pandas as pd

TN = 40.0
FP = 5
FN = 10
TP = 45
data = data = {
        "recall": [0.818],
        "precision": [0.9],
        "f1 score": [0.857],
    }
df = pd.DataFrame(data)


## test if it produces correct data frame
def test_metrics():
    res = metrics_function.calculate_metrics(TN, FP, FN, TP)

    pd.testing.assert_frame_equal(res, df)

def test_metrics_values():
    res = metrics_function.calculate_metrics(TN, FP, FN, TP)
    assert df.iat[0,0] == res.iat[0,0]
    assert df.iat[0,1] == res.iat[0,1]
    assert df.iat[0,2] == res.iat[0,2]

TN1 = 40.0
FP1 = 5
FN1 = 10
TP1 = 45
recall = TP1 / (TP1 + FN1)
precision = TP1 / (TP1 + FP1)
f1_score = (2 * precision * recall) / (precision + recall)

data1 = data = {
        "recall": [recall],
        "precision": [precision],
        "f1 score": [f1_score],
    }
df1 = pd.DataFrame(data1)

def test_metrics_round():

    res = metrics_function.calculate_metrics(TN, FP, FN, TP)

    assert df1.iat[0,0] != res.iat[0,0]
    assert df1.iat[0,1] == res.iat[0,1]
    assert df1.iat[0,2] != res.iat[0,2]


