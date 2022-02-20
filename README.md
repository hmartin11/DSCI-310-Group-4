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

To run the project, clone this repository and run the following commands in the terminal.

Pull the image from DockerHub:  
`docker pull dianali/dsci-310_group-4`  

After pulling the image:  
`docker run --rm -p 8888:8888 dianali/dsci-310_group-4`  

## License
This is an open-sourced project licensed under the MIT License. Please refer to LICENSE.md for more information.

