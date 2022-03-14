import pandas as pd
import numpy as np


#' Calculate summary statistics
#'
#' Creates a new data frame with with the same columns as input and 4 rows, 
#' listing the mean for each column present in the input data frame,
#' the standard deviation,
#' the minimum value for each column
#' and the maximum value for each column.
#'
#' @param data_frame A data frame with number values
#'
#' @return A data frame with four rows. 
#'   The first row (named mean) lists the mean of each column from the input data frame.
#'   The second row (named std) lists the standard deviation of each column from the input data frame.
#'   It will have the same number of columns as the columns present in input data frame.
#'
#' @export
#'
#' @examples
#' get_summary_stats(train_df)

def get_summary_stats(data_frame):
    # returns a data frame with with the same columns as input,
    # and 4 rows: mean, std, min and max


    try:
        if not isinstance(data_frame, pd.DataFrame):
            raise AttributeError("Invalid input: Not a DataFrame")
    except Exception as err:
        print("Something has gone wrong", err)
        return err
    
    try:
        df = data_frame.sort_values(by=list(df.columns), axis=0)
    except TypeError as err:
        print("Invalid Data: Not all numeric", err)
        return err

    df = df.describe()
    df.drop(labels=['count', '25%', '50%', '75%'], axis=0, inplace=True)

    return df