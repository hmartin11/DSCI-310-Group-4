# COMMENTS AUADFUABAKBF

all : results/figures/____.png results/figures/______.png results/________.csv results/_________.csv

# read data from url into csv
data/card_default_data.csv: scripts/read_data_from_url.py
	python3 scripts/read_data_from_url.py "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls" "data/card_default_data.csv"

# process and split data into train and test datasets
data/processed_train_data.csv data/processed_test_data.csv data/processed_X_train_data.csv data/processed_X_test_data.csv data/processed_y_train_data.csv data/processed_y_test_data.csv: scripts/preprocessing_data.py data/card_default_data.csv
	python3 scripts/preprocessing_data.py "data/card_default_data.csv" "data/"

# obtain tables and figures in created in  exploratory data analysis tables


clean :
	rm -f data/*.csv
	rm -f results/*.csv
	rm -f results/*.png