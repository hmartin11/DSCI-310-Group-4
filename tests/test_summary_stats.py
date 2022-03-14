import py
from src import summary_stats_function as ss



import pytest  
import pandas as pd
import numpy as np

# Tests that not passing a dataframe will result in an AttributeError
def test_not_dataframe():

    #invalid object type input List
    bad_list = [1,2,3,4,5]

    expected = AttributeError
    actual = ss.get_summary_stats(bad_list)
    assert isinstance(actual,expected)


# Tests that non-number values in dataframe will result in a TypeError
def test_not_number_data():

    #invalid entry type String in one column
    d = {'Name':pd.Series(['A','B','C','D','E']),
    'Age':pd.Series([1,2,3,4,5]),
    'Score':pd.Series([0,0,0,0,0])}
    df = pd.DataFrame(d)

    expected = TypeError
    actual = ss.get_summary_stats(df)
    assert isinstance(actual,expected)


# Tests that the outputs of a valid input are correct
def test_valid_dataframe():

    # each column tests both whole numbers, integers and decimals data inputs
    d = {'ID':pd.Series([0,1,2,3,4]),
    'Age':pd.Series([0,-10,20,30,-40]),
    'Score':pd.Series([111.11,111.11,111.11,111.11,111.11])}
    df = pd.DataFrame(d)

    exp_d = {'ID':pd.Series([df['ID'].mean(),df['ID'].std(),0,4]),
    'Age':pd.Series([df['Age'].mean(),df['Age'].std(),-40,30]),
    'Score':pd.Series(111.11,0,111.11,111.11)}
    exp_d.index = ['mean','std','min','max']
    expected = pd.DataFrame(exp_d)
    
    actual = ss.get_summary_stats(df)
    
    assert actual == expected
    