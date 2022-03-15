import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src import function_count_plot


data = pd.DataFrame(np.linspace(4,7,10), columns=["x1"])
data1 = pd.DataFrame(np.linspace(7,4,14), columns=["x1"])
labels = ["0","1"]
plot = count_plot(data, x, y, "Count Plot")
fig, ax = plt.subplots()

def test_return_type():
    """
    Test for the correct return type of the function is an Axes object
    """
    assert type(plot) == type(ax)

def test_readability():
    """
    Test for the correct label for X,y axis, legend and title
    """
    assert plot.get_xlabel() == "PAY_0"
    assert plot.get_ylabel() == "Count"
    assert plot.get_legend().get_texts()[0].get_text() == labels[0]
    assert plot.get_legend().get_texts()[1].get_text() == labels[1]
    assert plot.get_title() == "Count Plot"
