# This script preprocesses data and splits data into training and test splits.
# This script takes 2 arguments (input_path, output_path)
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


def preprocessing_data(input_path, output_path):
    
    df = pd.read_csv(input_path,sep = ",")
    # rename column to get rid of spaces
    df.rename(columns = {"default payment next month":"default_payment"}, inplace = True)
    train_df, test_df = pp.preprocess(df, 0.8, 200)
    
    # write dataframe to filepath
    train_df.to_csv(output_path, index = False)
    test_df.to_csv(output_path, index = False)

def main():
    ""
    input_path = 'data/card_default_data.csv'
    output_path = 'data/processed_df'   
    preprocessing_data(input_path, output_path)

if __name__ == "__main__":
    main()
