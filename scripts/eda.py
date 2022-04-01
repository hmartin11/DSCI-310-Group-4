import os
import sys
sys.path.append('.')
from src.function_count_plot import count_plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.summary_stats_function import get_summary_stats


def make_heatmap(input_path, output_path):

    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize=(25,25))
    sns.heatmap(train_df.corr(),cbar=True,annot=True,cmap='Reds')
    plt.savefig(output_path)

def make_limit_dist(input_path, output_path1):
    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize = (16,9))
    sns.distplot(train_df['LIMIT_BAL'],kde=True,bins=50, rug = True, color="green")
    plt.savefig(output_path1) 


def make_repayment_hist(input_path, output_path2):
    train_df = pd.read_csv(input_path,sep = ",")
    for column in train_df[["PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]]:
        count_plot(data=train_df, x=column, name ="Repayment status:" + column)
        #fig = plot.fig
        output_path2 = output_path2 + str(column) + ".png"
        plt.savefig(output_path2) 

def make_class_imbalance(input_path, output_path3):
    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize=(6,4))

    default_plot = sns.countplot(x = "default_payment",data = train_df)
    plt.ylim(0,25000)
    total = float(len(train_df))
    for p in default_plot.patches:
        default_plot.annotate((str(100* p.get_height()/total) + "%"), (p.get_x()+0.32, p.get_height()+1000), ha="center")
    
    plt.savefig(output_path3) 

def make_summary_table(input_path, output_path4):
    train_df = pd.read_csv(input_path,sep = ",")
    summary = get_summary_stats(train_df)
    summary.to_csv(output_path4)






def main():

    input_path = "data/processed_train_data.csv"
    output_path = 'data/heatmap.png'
    output_path1 = 'data/limit_bal_dist.png'
    output_path2 = 'data/repayment_status_'
    output_path3 = 'data/class_imbalance.png'
    output_path4 = 'data/summary_stats.csv'

    make_heatmap(input_path, output_path)
    make_limit_dist(input_path, output_path1)
    make_repayment_hist(input_path, output_path2)
    make_class_imbalance(input_path, output_path3)
    make_summary_table(input_path, output_path4)

if __name__ == "__main__":
    main()




