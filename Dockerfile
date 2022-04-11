# Obtain image from this source
FROM jupyter/scipy-notebook:8f0a73e76d17
 
# Install python3 packages for scripts
RUN pip3 install group4package==0.1.1 \
    argparse==1.4.0 \
    matplotlib==3.5.1 \
    numpy==1.21.5 \
    pandas==1.4.2 \
    seaborn==0.11.2 \
    xgboost==1.5.1 \
    scikit-learn==1.0.2 \
    plotly==5.6.0 \
    pytest==7.1.0 \
    pandoc==2.1

# Install R packages with conda for R Markdown
RUN conda install --yes --quiet --channel conda-forge \
    python=3.9.7\
    r-base=4.0.5 \
    r-tidyverse=1.3.1 \
    r-tidymodels=0.1.4 \
    r-rmarkdown=2.13 \
    r-bookdown=0.25 \
    r-tinytex=0.37 \
    r-knitr=1.37 

USER root

RUN apt-get update && apt-get -y install --no-install-recommends lmodern
