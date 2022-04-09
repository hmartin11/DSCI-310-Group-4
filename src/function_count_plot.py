import matplotlib.pyplot as plt
import seaborn as sns

# ' Plot a Countplots
# '
# 'Creates countplots for data frame with all the given x and y values,
# '
# ' @param A data frame with all the values of which we want the countplots
# ' @param array a list of numbers which represents the different payments for x-values
# ' @param string the name of the plot
# '
# ' @return A plot of the counts between two parameters of the given dataframe.
# '         The plot should have a x label, a y label and a title.
# '
# ' @export
# '
# ' @examples
# ' count_plot(train_df, x, "Count plot")


def count_plot(df, x, name):
    # returns a figure of a counts between two parameters of the given dataframe,
    # and has a given title, and correct x and y labels.

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
    plt.xlabel(str(x))
    plt.ylabel("count")
    plt.title(name)
    return fig
