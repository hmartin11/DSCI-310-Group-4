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
# ' @return An plot of the counts between two parameters of the given data frame.
# '         The plot should have a x label, a y label and a title.
# '
# ' @export
# '
# ' @examples
# ' count_plot(train_df, x, "Count plot")


def count_plot(data, x, name):
    fig = sns.countplot(data=data, hue="default_payment", x=x)
    plt.xlabel(str(x))
    plt.ylabel("count")
    plt.title(name)
    return fig
