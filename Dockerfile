# Obtain image from this source
FROM ubcdsci/jupyterlab

# Installing matplotlib
FROM ubuntu:20.10
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install matplotlib=3.5.1
 
# Install python package with package
RUN conda install --yes --quiet --channel conda-forge \
    numpy=1.22.2 \
    pandas=1.4.1 \
    seaborn=0.11.2 \
    xgboost=1.5.1 \
    scikit-learn=1.0.2 \
    plotly=5.6.0

