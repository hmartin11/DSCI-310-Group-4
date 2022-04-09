from src import function_count_plot as c
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest



data = pd.DataFrame({"PAY_0": [-2, 1, 0, 0, -1], "default_payment": [1, 1, 0, 1, 0]})
labels = ["0", "1"]
plot = c.count_plot(data, "PAY_0", "Count Plot")
fig, ax = plt.subplots()

def test_readability():
    """Test for the correct label for X,y axis, legend and title"""
    assert plot.get_xlabel() == "PAY_0"
    assert plot.get_ylabel() == "count"
    assert plot.get_legend().get_texts()[0].get_text() == labels[0]
    assert plot.get_legend().get_texts()[1].get_text() == labels[1]
    assert plot.get_title() == "Count Plot"
