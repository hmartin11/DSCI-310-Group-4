# DSCI 310 Group 4
# Last Modified: April 2022

# Makefile that runs the project's scripts and analysis

all : results/heatmap.png results/limit_bal_dist.png results/class_imbalance.png results/repayment_status_PAY_0.png results/repayment_status_PAY_2.png results/repayment_status_PAY_3.png results/repayment_status_PAY_4.png results/repayment_status_PAY_5.png results/repayment_status_PAY_6.png results/summary_stats.csv 

# read data from url into csv and write to file
data/card_default_data.csv: scripts/read_data_from_url.py
	python3 scripts/read_data_from_url.py

# preprocess and split data into train and test datasets
data/processed_train_data.csv data/processed_test_data.csv data/processed_X_train_data.csv data/processed_X_test_data.csv data/processed_y_train_data.csv data/processed_y_test_data.csv: scripts/preprocessing_data.py data/card_default_data.csv
	python3 scripts/preprocessing_data.py

# obtain tables and figures in created in  exploratory data analysis and write to file (ie. heatmap, )
results/heatmap.png results/limit_bal_dist.png results/class_imbalance.png results/repayment_status_PAY_0.png results/repayment_status_PAY_2.png results/repayment_status_PAY_3.png results/repayment_status_PAY_4.png results/repayment_status_PAY_5.png results/repayment_status_PAY_6.png results/summary_stats.csv: scripts/preprocessing_data.py data/processed_train_data.csv
	python3 scripts/eda.py

# create model 

    
clean :
	rm -f data/*.csv
	rm -f results/*.csv
	rm -f results/*.png