# This script downloads data from web and saves data locally.
# This script takes 2 arguments (url, file path to write the file to along with its file name)

# Usage: python3 scripts/read_data_from_url.py <url> <filepath>
# url: Website url from which we source our data from for the project
# output_path:  Path of where to locally write the file


# load libraries/packages or source functions from other scripts
import pandas as pd

import ssl

# parse arguments
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('url', type=str,
                    help='Website url from which we source our data from for the project')
parser.add_argument('output_path', type=str,
                    help='Path of where to locally write the file')

args = parser.parse_args()

# load the dataset
def read_data_from_url(url, output_path):
    ssl._create_default_https_context = ssl._create_unverified_context
    # load the dataset
    df = pd.read_excel(url, skiprows=1)
    # write dataframe to filepath
    df.to_csv(output_path, index = False)

def main(url,output_path):   
    read_data_from_url(url, output_path)

if __name__ == "__main__":
    main(args.url, args.output_path)
