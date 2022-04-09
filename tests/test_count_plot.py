from src import function_count_plot as c
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest


data = pd.DataFrame({"PAY_0": [-2, 1, 0, 0, -1], "default_payment": [1, 1, 0, 1, 0]})
labels = ["0", "1"]
plot = c.count_plot(data, "PAY_0", "Count Plot")
fig, ax = plt.subplots()

# Tests that not passing a dataframe will result in an AttributeError
def test_not_dataframe():

    # invalid object type input List
    bad_dataframe = [1, 2, 3, 4, 5]

    expected = AttributeError
    actual = c.count_plot(bad_dataframe, "PAY_0", "Count Plot")
    assert isinstance(actual, expected)

# Tests that not passing a string for title will result in an AttributeError
def test_not_string():

    # invalid object type input List
    data = pd.DataFrame({"PAY_0": [-2, 1, 0, 0, -1], "default_payment": [1, 1, 0, 1, 0]})
    bad_dataframe = [1, 2, 3, 4, 5]

    expected = AttributeError
    actual = c.count_plot(data, "PAY_0", bad_dataframe)
    assert isinstance(actual, expected)

# Tests that empty dataframe will return dataframe
def test_empty_dataframe():

    # empty dataframe with column names
    df = pd.DataFrame(columns=["PAY_0", "default_payment"])

    expected = df
    actual = c.count_plot(df, "PAY_0", "Count Plot")
    pd.testing.assert_frame_equal(actual, expected)


def test_readability():
    # Test for the correct label for x,y axis, legend and title
    assert plot.get_xlabel() == "PAY_0"
    assert plot.get_ylabel() == "count"
    assert plot.get_legend().get_texts()[0].get_text() == labels[0]
    assert plot.get_legend().get_texts()[1].get_text() == labels[1]
    assert plot.get_title() == "Count Plot"
