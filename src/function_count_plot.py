import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ' Plot a Countplots
# '
# 'Creates countplots for data frame with all the given x and y values,
# '
# ' @param A data frame with all the values of which we want the countplots
# ' @param string the column name heading for x-values
# ' @param string the name of the plot
# '
# ' @return An plot of the counts between two parameters of the given data frame.
# '         The plot should have a x label, a y label and a title.
# '
# ' @export
# '
# ' @examples
# ' count_plot(train_df, x, "Count plot")


def count_plot(df, x, name):
    try:
        if not isinstance(df, pd.DataFrame):
            raise AttributeError("Invalid input: df is not a DataFrame")
            
        if not isinstance(name, str):
            raise AttributeError("Invalid input: name is not a String")
        
        if not isinstance(x, str):
            raise AttributeError("Invalid input: x is not a String")
            
    except Exception as err:
        print("Something has gone wrong", err)
        return err

    if df.empty:
        print("DataFrame is empty!")
        return df
    
    fig = sns.countplot(data=df, hue="default_payment", x=x)
    plt.xlabel(str(x), fontsize=16)
    plt.ylabel("count", fontsize=16)
    plt.title(name, fontsize = 22)
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    return fig
