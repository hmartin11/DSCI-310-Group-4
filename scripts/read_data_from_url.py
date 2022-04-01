# This script downloads data from web and saves data locally.
# This script takes 2 arguments (url, file path to write the file to along with its file name)
# Usage: *.py //update later

# load libraries/packages or source functions from other scripts
import pandas as pd

import ssl



# load the dataset
def read_data_from_url(url, filepath):
    ssl._create_default_https_context = ssl._create_unverified_context
    # load the dataset
    df = pd.read_excel(url, skiprows=1)
    # write dataframe to filepath
    df.to_csv(filepath, index = False)

def main():

    
    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls"
    path = 'data/card_default_data.csv'   
    read_data_from_url(url, path)

if __name__ == "__main__":
    main()
