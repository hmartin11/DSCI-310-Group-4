import pandas as pd
import numpy as np


#' Calculate summary statistics
#'
#' Creates a new data frame with only the numerical columns of input and 4 rows,
#' listing the mean for each column present in the input data frame,
#' the standard deviation,
#' the minimum value for each column
#' and the maximum value for each column.
#' Columns in input that are categorical or not fully numerical are not included in returned dataframe
#'
#' @param data_frame A data frame with number values
#'
#' @return A data frame with four rows.
#'   The first row (named mean) lists the mean of each column from the input data frame.
#'   The second row (named std) lists the standard deviation of each column from the input data frame.
#'   It will have the same number of columns as the fully-numerical columns present in input data frame.
#'
#' @export
#'
#' @examples
#' get_summary_stats(train_df)


def get_summary_stats(df):
    # returns a data frame with the same number of columns as fully numerical columns input,
    # and 4 rows: mean, std, min and max

    try:
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Invalid input: Not a DataFrame")
    except Exception as err:
        print("Something has gone wrong", err)
        return err

    if df.empty:
        print("DataFrame is empty!")
        return df

    df = df.select_dtypes(include=np.number)

    new_df = pd.DataFrame(index=["mean", "std", "min", "max"])

    for column in df:

        new_df[column] = (
            df[column].mean(),
            df[column].std(),
            df[column].min(),
            df[column].max(),
        )

    return new_df
