# Obtain image from this source
FROM jupyter/scipy-notebook:8f0a73e76d17
 
# Install python3 packages for scripts
RUN pip3 install argparse==1.4.0 \
    matplotlib==3.5.1 \
    numpy==1.22.2 \
    pandas==1.4.1 \
    seaborn==0.11.2 \
    xgboost==1.5.1 \
    scikit-learn==1.0.2 \
    plotly==5.6.0 \
    pytest==7.1.0

# Install python package with conda for *.ipynb
RUN conda install --yes --quiet --channel conda-forge \
    matplotlib=3.5.1 \
    numpy=1.22.2 \
    pandas=1.4.1 \
    seaborn=0.11.2 \
    xgboost=1.5.1 \
    scikit-learn=1.0.2 \
    plotly=5.6.0 \
    pytest=7.1.0

USER root

RUN apt-get update && apt-get install -y --no-install-recommends build-essential r-base python3.9 python3-pip python3-setuptools python3-dev

# Install required dependencies for R Markdown
RUN Rscript -e "install.packages('knitr', dependencies = TRUE)"
RUN Rscript -e "install.packages('rmarkdown')"
RUN Rscript -e "install.packages('bookdown')"
RUN Rscript -e "tinytex::install_tinytex()"
