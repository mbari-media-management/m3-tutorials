FROM ubuntu

RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    apt-transport-https \
    apt-utils \
    build-essential \
    cmake \
    curl \
    npm \
    software-properties-common \
    unzip \
  && apt-add-repository ppa:openjdk-r/ppa \
  && apt-get install -y --no-install-recommends \
    openjdk-8-jdk \
  && rm -rf /var/lib/apt/lists/*

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV PATH=/root/miniconda3/bin:$PATH

RUN conda config --append channels conda-forge \
  && conda install -y \
      beakerx \
      h5py \
      ipywidgets \
      jupyter \
      jupyterlab \
      matplotlib \
      netcdf4 \
      pandas \
      scikit-learn \
      seaborn \
  && conda update conda \
  && conda clean --yes --tarballs --packages \
  && conda build purge-all

RUN beakerx install \
  && jupyter labextension install @jupyter-widgets/jupyterlab-manager

RUN apt-get update \
  && apt-get install -y graphviz xvfb python-opengl \
  && pip install --upgrade pip \
  && pip install graphviz \
  && rm -rf /var/lib/apt/lists/*
  # pip install graphviz xgboost

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888

CMD xvfb-run -s "-screen 0 1400x900x24" jupyter lab --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
