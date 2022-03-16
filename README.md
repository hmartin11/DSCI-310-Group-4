# DSCI-310-Group-4

## Contributors

* Jordan Yu
* Shravan Chaniara
* Diana Liang
* Hannah Martin

## Summary
### Default payments in Taiwan and comparison of the predictive accuracy of probability of default

Financial institutions incur monetary loss when a client or borrower is unable to pay their interest or their initial principal on time. Thus, it is necessary for such institutions to assess the risk that potential borrowers cannot repay their loan in determining their eligibility for the loan in the first place. The present study endeavors to answer the question "Is there a way to effectively predict whether or not a client will default on their credit card payment?" and uncover the most significant features that contribute to the higher likelihood of defaulting. The result of predictive accuracy of the projected likelihood of default will be more beneficial than the binary result of categorization - credible or not credible customers - from the standpoint of risk management.

The project consists of following files:
* README.md
* CODE_OF_CONDUCT.md
* CONTRIBUTING.md
* data/
* tests/
* src/
* analysis.ipynb
* Dockerfile
* .github/workflows/publish_docker_image.yml
* LICENSE.md

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

Access the [Dockerfile](https://github.com/DSCI-310/DSCI-310-Group-4/blob/main/Dockerfile) and [Docker image](https://hub.docker.com/repository/docker/dianali/dsci-310_group-4) here.

To run the project, follow the following steps:

1. Launch Docker, otherwise the following steps may not work. If you have not installed Docker, follow the hardware specific instructions [here](https://docs.docker.com/get-docker/)
2. Open the terminal and run the following commands:
   + Pull the image from DockerHub:```docker pull dianali/dsci-310_group-4```
   + After pulling the image:```docker run --rm -p 8888:8888 -v /$(pwd):/home/group-4-project dianali/dsci-310_group-4```  
3. Copy and paste the resulting link output beginning with `http://127.0.0.1:8888/lab?token=<your token>`into a web browser to launch Jupyter Lab
    
4. Once in JupyterLab, you should be in an empty directory with a folder '/work'. Open a Terminal from within JupyterLab
    
5. Clone this repository onto the local machine by running the following command:```git clone https://github.com/DSCI-310/DSCI-310-Group-4```
   + NOTE: This will likely require a GitHub account and an active authentication token, cloning using the SSH link may not work.
   + For more guidance on cloning, follow the instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    
6. Once you have successfully cloned the project, open the project folder "DSCI-310-Group-4" and run the Jupyter Notebook. *Voila!*

## Testing
After recreating the project environment used during development by following the steps on "How to Run the Project", test the code by running the command line ```pytest``` in the terminal from the root project directory.

## License
This is an open-sourced project licensed under the MIT License. Please refer to LICENSE.md for more information.

