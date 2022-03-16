import py
from src import summary_stats_function as ss


import pytest
import pandas as pd
import numpy as np

# Tests that not passing a dataframe will result in an AttributeError
def test_not_dataframe():

    # invalid object type input List
    bad_list = [1, 2, 3, 4, 5]

    expected = AttributeError
    actual = ss.get_summary_stats(bad_list)
    assert isinstance(actual, expected)


# Tests that empty dataframe will return dataframe
def test_empty_dataframe():

    # empty dataframe with column names
    df = pd.DataFrame(columns=["species", "name", "age"])

    expected = df
    actual = ss.get_summary_stats(df)
    pd.testing.assert_frame_equal(actual, expected)


# Tests that the outputs of a valid input are correct
def test_valid_dataframe():

    # each column tests both whole numbers, integers and decimals data inputs
    data = data = {
        "ID": [0, 1, 2, 3, 4],
        "Age": [12, 45, 20, 30, 18],
        "Score": [10.0, 10.0, 10.0, 10.0, 10.0],
    }
    df = pd.DataFrame(data)

    exp_df = pd.DataFrame(
        {
            "ID": [df["ID"].mean(), df["ID"].std(), 0, 4],
            "Age": [df["Age"].mean(), df["Age"].std(), 12, 45],
            "Score": [10.0, 0.0, 10.0, 10.0],
        },
        index=["mean", "std", "min", "max"],
    )

    # exp_df = pd.DataFrame(exp_data)

    actual = ss.get_summary_stats(df)

    # assert actual == expected
    pd.testing.assert_frame_equal(actual, exp_df)


# Tests that the outputs of a valid input are correct but with categorical data
def test_valid_dataframe_with_categorical():

    # columns with numerical, categorical and mixed data inputs
    data = data = {
        "ID": [0, 1, 2, 3, 4],
        "Age": [0, -10, 20, 30, -40],
        "Sex": ["F", "M", "F", "F", "M"],
        "Score": [10.0, 10.0, 10.0, 10.0, 10.0],
        "Random": ["high", "low", 0, "high", 0],
    }
    df = pd.DataFrame(data)

    exp_df = pd.DataFrame(
        {
            "ID": [df["ID"].mean(), df["ID"].std(), 0, 4],
            "Age": [df["Age"].mean(), df["Age"].std(), -40, 30],
            "Score": [10.0, 0.0, 10.0, 10.0],
        },
        index=["mean", "std", "min", "max"],
    )

    actual = ss.get_summary_stats(df)

    # assert actual == expected
    pd.testing.assert_frame_equal(actual, exp_df)
