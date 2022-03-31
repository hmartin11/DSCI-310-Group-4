# This script preprocesses data and splits data into training and test splits.
# This script takes 3 arguments (input_path, output_path_train, output_path_test)
# Usage: *.py //update later
# input_path:   Path to the data file to be read in
# output_path:  Path of where to locally write the file

# load libraries/packages or source functions from other scripts

#from src import preprocess as pp
import os
import sys
sys.path.append('.')
from src import preprocess as pp

import pandas as pd




#src.preprocess import preprocess as pp


def preprocessing_data(input_path, output_path_train, output_path_test):

    df = pd.read_csv(input_path,sep = ",")
    # rename column to get rid of spaces
    df.rename(columns = {"default payment next month":"default_payment"}, inplace = True)
    train_df, test_df = pp.preprocess(df, 0.8, 200)
    
    # write dataframe to filepath
    train_df.to_csv(output_path_train, index = False)
    test_df.to_csv(output_path_test, index = False)

def main():
    ""
    input_path = 'data/card_default_data.csv'
    output_path_train = 'data/processed_train_data.csv'   
    output_path_test = 'data/processed_test_data.csv'   
    preprocessing_data(input_path, output_path_train, output_path_test)

if __name__ == "__main__":
    main()
