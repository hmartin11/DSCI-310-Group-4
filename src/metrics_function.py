import pandas as pd
import numpy as np


## parameters: TN, FP, FN, TP

#' calculate_metrics 
#'
#'
#' A function for calculating classification metrics including recall, precision and f1-score
#' @param TN integer representing the number of true negatives classified by model
#' @param TP integer representing the number of true postives classified by model
#' @param FP integer representing the number of false positives classified by model
#' @param FN integer representing the number of false negatives classified by model
#'
#' @return
#'  a pandas data frame with one row and 3 columns
#'
#' @examples
#' calculate_metrics(TN=87, FP=14, FN=12, TP=70)


def calculate_metrics(TN, FP, FN, TP):

    recall = TP / (TP + FN)
    precision = TP / (TP + FP)
    f1_score = (2 * precision * recall) / (precision + recall)



    data = {
        "recall": [round(recall, 3)],
        "precision": [round(precision, 3)],
        "f1 score": [round(f1_score, 3)],
    }




    return pd.DataFrame(data)

