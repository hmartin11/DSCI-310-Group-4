import os
import sys
sys.path.append('.')
from src.function_count_plot import count_plot as cp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_heatmap(input_path, output_path):

    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize=(25,25))
    sns.heatmap(train_df.corr(),cbar=True,annot=True,cmap='Reds')
    plt.savefig(output_path)



def main():

    input_path = "data/processed_train_data.csv"
    output_path = 'data/heatmap.png'

    make_heatmap(input_path, output_path)

if __name__ == "__main__":
    main()




