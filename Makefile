# DSCI 310 Group 4
# Last Modified: April 2022

# Makefile that runs the project's scripts and analysis

# build all the artifacts and files used for project analysis
all : reports/final_report.html reports/final_report.pdf

# read data from url into csv and write to file
data/card_default_data.csv: scripts/read_data_from_url.py
	python3 scripts/read_data_from_url.py "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls" "data/raw_data/card_default_data.csv"

# preprocess and split data into train and test datasets
data/processed_train_data.csv data/processed_test_data.csv data/processed_X_train_data.csv data/processed_X_test_data.csv data/processed_y_train_data.csv data/processed_y_test_data.csv: scripts/read_data_from_url.py data/card_default_data.csv
	python3 scripts/preprocessing_data.py "data/raw_data/card_default_data.csv" "data/processed_data/"

# obtain tables and figures in created in  exploratory data analysis and write to file (ie. heatmap, )
results/heatmap.png results/limit_bal_dist.png results/class_imbalance.png results/repayment_status_PAY_0.png results/repayment_status_PAY_2.png results/repayment_status_PAY_3.png results/repayment_status_PAY_4.png results/repayment_status_PAY_5.png results/repayment_status_PAY_6.png results/summary_stats.csv: scripts/preprocessing_data.py data/processed_train_data.csv
	python3 scripts/eda.py "data/processed_data/processed_train_data.csv" "results/"

# perform modeling and summarize results as figures and tables and write to file
results/scores_1.csv results/scores_2.csv results/coefs.csv results/roc.png results/confusion_matrix.png results/metrics.csv: scripts/train_test_models.py data/processed_X_test_data.csv data/processed_y_test_data.csv data/processed_X_train_data.csv data/processed_y_train_data.csv
	python3 scripts/train_test_models.py "data/processed_data/processed_X_train_data.csv" "data/processed_data/processed_y_train_data.csv" "data/processed_data/processed_X_test_data.csv" "data/processed_data/processed_y_test_data.csv" "results/"

# render analysis report and save it as a html document
reports/final_report.html: reports/final_report.Rmd reports/references.bib results/heatmap.png results/limit_bal_dist.png results/class_imbalance.png results/repayment_status_PAY_0.png results/repayment_status_PAY_2.png results/repayment_status_PAY_3.png results/repayment_status_PAY_4.png results/repayment_status_PAY_5.png results/repayment_status_PAY_6.png results/summary_stats.csv results/scores_1.csv results/scores_2.csv results/coefs.csv results/roc.png results/confusion_matrix.png results/metrics.csv
	Rscript -e "rmarkdown::render('reports/final_report.Rmd', 'html_document')"

# render analysis report and save it as a pdf document
reports/final_report.pdf: reports/final_report.Rmd reports/references.bib results/heatmap.png results/limit_bal_dist.png results/class_imbalance.png results/repayment_status_PAY_0.png results/repayment_status_PAY_2.png results/repayment_status_PAY_3.png results/repayment_status_PAY_4.png results/repayment_status_PAY_5.png results/repayment_status_PAY_6.png results/summary_stats.csv results/scores_1.csv results/scores_2.csv results/coefs.csv results/roc.png results/confusion_matrix.png results/metrics.csv
	Rscript -e "rmarkdown::render('reports/final_report.Rmd', 'pdf_document')"

clean :
	rm -f data/raw_data/*.csv
	rm -f data/processed_data/*.csv
	rm -f results/*.csv
	rm -f results/*.png
	rm -f reports/final_report.html
	rm -f reports/final_report.pdf
	rm -f reports/final_report.aux
	rm -f reports/final_report.out