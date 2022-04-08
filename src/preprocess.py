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
def preprocess(df, train_frac, seed):

    try:
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Invalid input: df is not a DataFrame")
        
        if not isinstance(train_frac, float):
            raise AttributeError("Invalid input: train_frac is not a float")
    
        if not train_frac < 1 and train_frac > 0:
            raise AttributeError("Invalid input: train_frac is not a float between 0 and 1")
            
    
        if not isinstance(seed, int):
            raise AttributeError("Invalid input: Seed is not an integer")
            
    except Exception as err:
        print("Something has gone wrong", err)
        return err

    if df.empty:
        print("DataFrame is empty!")
        return df
    
    
    df = df.dropna()
    train = df.sample(frac=train_frac, random_state=seed)
    test = df.drop(train.index)
    return train, test
