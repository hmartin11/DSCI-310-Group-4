#' drop all rows containing null values then split the df into training and testing part
#'
#' @param dataframe The shuffled data frame
#' @param train_frac The percent that ends up in the training set (range 0-1).
#' @param seed Set the seed for training/testing set split
#'
#' @return training and testing dataframes without missing/null values
#'
#' @export
#'
#' @examples
#' preprocess(dataframe, 0.8, 20)


def preprocess(df, train_frac, seed):
    df = df.dropna()
    train = df.sample(frac=train_frac, random_state=seed)
    test = df.drop(train.index)
    return train, test
