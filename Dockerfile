# Obtain image from this source
FROM jupyter/scipy-notebook:8f0a73e76d17
 
# Install python package with package
RUN conda install --yes --quiet --channel conda-forge \
    matplotlib=3.5.1 \
    numpy=1.22.2 \
    pandas=1.4.1 \
    seaborn=0.11.2 \
    xgboost=1.5.1 \
    scikit-learn=1.0.2 \
    plotly=5.6.0 \
    pytest=7.1.0

# Install python3 package with package
RUN pip3 install argparse==1.4.0

# Install required dependencies for R Markdown
RUN Rscript -e "install_version('knitr', version = '1.38')"
RUN Rscript -e "install_version('tidyverse', version = '1.3.1')"
