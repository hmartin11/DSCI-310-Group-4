# DSCI-310-Group-4

## Contributors

* Jordan Yu
* Shravan Chaniara
* Diana Liang
* Hannah Martin

## Summary
### Default payments in Taiwan and comparison of the predictive accuracy of probability of default

Financial institutions incur monetary loss when a client or borrower is unable to pay their interest or their initial principal on time. Thus, it is necessary for such institutions to assess the risk that potential borrowers cannot repay their loan in determining their eligibility for the loan in the first place. The present study endeavors to answer the question "Is there a way to effectively predict whether or not a client will default on their credit card payment?" and uncover the most significant features that contribute to the higher likelihood of defaulting. The result of predictive accuracy of the projected likelihood of default will be more beneficial than the binary result of categorization - credible or not credible customers - from the standpoint of risk management.

The project consists of following files or folders:
* README.md
* LICENSE.md
* CODE_OF_CONDUCT.md
* CONTRIBUTING.md
* data/
* reports/
* tests/
* src/
* scripts/
* results/
* .github/workflows/
* analysis.ipynb
* Dockerfile
* Makefile
* DSCI-310-Group-4.Rproj

The main data anaylsis and the methods used for the project are in the analysis.ipynb.

## How to Run the Project
The project was developed in Python (version 3.9.7) and utilizes the following dependencies:

|Dependency  |   Version|
|------------|----------|
|pandas      |   1.4.1  |
|numpy       |   1.22.2 |
|matplotlib  |   3.5.1  |
|plotly      |   5.6.0  |
|seaborn     |   0.11.2 |
|scikit-learn|   1.0.2  |
|xgboost     |   1.5.1  |
|pytest      |   7.1.0  |
|argparse    |   1.4.0  |
|pandoc      |   2.1    |
|r-base      |   4.0.5  |
|r-tidyverse |   1.3.1  |
|r-tidymodels|   0.1.4  |
|r-rmarkdown |   2.13   |
|r-bookdown  |   0.25   |
|r-tinytex   |   0.37   |
|r-knitr     |   1.37   |

Access the [Dockerfile](https://github.com/DSCI-310/DSCI-310-Group-4/blob/main/Dockerfile) and [Docker image](https://hub.docker.com/repository/docker/dianali/dsci-310_group-4) here.

To run the project, follow the following steps:

### Running the Project via Docker

1. Launch Docker, otherwise the following steps may not work. If you have not installed Docker, follow the hardware specific instructions [here](https://docs.docker.com/get-docker/)
2. Clone this repository onto the local machine by running the following command:```git clone https://github.com/DSCI-310/DSCI-310-Group-4```
   + NOTE: This will likely require a GitHub account and an active authentication token, cloning using the SSH link may not work.
   + For more guidance on cloning, follow the instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
3. Once you have successfully cloned the project, open the terminal and navigate to the root of this repository using ```cd <folder name or path to project folder>```. If successful, typing ```pwd``` should return ```path/to/project/folder/DSCI-310-Group-4```
4. Run the following commands:
   + Pull the image from DockerHub:```docker pull dianali/dsci-310_group-4:v0.24.0```
   + After pulling the image:```docker run --rm -p 8888:8888 -v /$(pwd):/home/jovyan/work/DSCI-310-Group-4 dianali/dsci-310_group-4``` 
5. Copy and paste the resulting link output beginning with `http://127.0.0.1:8888/lab?token=<your token>`into a web browser to launch Jupyter Lab  
6. Once in JupyterLab, you should be in an empty directory with a folder '/work'. Open the 'work' folder.
7. Open the project folder "DSCI-310-Group-4" and run the Jupyter Notebook. *Voila!*

## Testing
After recreating the project environment used during development by following the steps on "How to Run the Project", test the code by running the command line ```pytest``` in the terminal from the root project directory from within JupyterLab.

## Running Scripts
After recreating the project environment used during development by following the steps on "How to Run the Project", test the code by running the command line ```make all``` in the terminal from the root project directory.

To clean the workspace, run ```make clean```

### Running the file via MakeFile:

Via MakeFile
1. clone the repository (same step as in the docker version)

2. Install all dependencies listed above

3. Open terminal, and inside the root project directory run: 

```make all```

 This creates the report.

To reset the repository run the following in terminal 

```make clean```


## License
This is an open-sourced project licensed under the MIT License. Please refer to LICENSE.md for more information.

