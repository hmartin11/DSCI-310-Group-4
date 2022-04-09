# A third script that reads the data from the second script, performs the exploratory data analysis and summarizes the analysis as a figure(s) and a table(s). 
# These analysis artifacts should be written to files. This should take at least two arguments: (path/filename pointing to the data, a path/filename prefix where to write the figure(s)/table(s) to and what to call it (e.g., results/this_analysis))

# Usage: python3 scripts/preprocessing_data.py <input_path> <output_path>
# input_path:   Path to the data file to be read in
# output_path:  Path of where to locally write the file

# load libraries/packages or source functions from other scripts

import os
import sys
sys.path.append('.')
from src.function_count_plot import count_plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.summary_stats_function import get_summary_stats

# parse arguments
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_path', type=str,
                    help='Path to the data file to be read in')
parser.add_argument('output_path', type=str,
                    help='Path of where to locally write the file')

args = parser.parse_args()



def make_heatmap(input_path, output_path):

    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize=(20,20))
    sns.heatmap(train_df.corr(),cbar=True,annot=True,cmap='Reds')
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.savefig(output_path)

def make_limit_dist(input_path, output_path1):
    train_df = pd.read_csv(input_path,sep = ",")
    plt.figure(figsize = (16,9))
    sns.distplot(train_df['LIMIT_BAL'],kde=True,bins=50, rug = True, color="green")
    plt.title("Limit Balance Distribution", fontsize = 20)
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel("Limit Balance", fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.savefig(output_path1) 


def make_repayment_hist(input_path, output_path22):
    train_df = pd.read_csv(input_path,sep = ",")
    for column in train_df[["PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]]:
        count_plot(df=train_df, x=column, name ="Repayment status:" + column)
        #fig = plot.fig
        #plt.rcParams.update({'font.size': 22})
        plt.rc('figure', titlesize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
      
        output_path2 = output_path22+ str(column) + ".png"
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






def main(input_path, output_path):
    output_path0 = output_path + 'heatmap.png'
    output_path1 = output_path + 'limit_bal_dist.png'
    output_path2 = output_path + 'repayment_status_'
    output_path3 = output_path + 'class_imbalance.png'
    output_path4 = output_path + 'summary_stats.csv'

    make_heatmap(input_path, output_path0)
    make_limit_dist(input_path, output_path1)
    make_repayment_hist(input_path, output_path2)
    make_class_imbalance(input_path, output_path3)
    make_summary_table(input_path, output_path4)

if __name__ == "__main__":
    main(args.input_path, args.output_path)




