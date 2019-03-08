ARG CUDA_VERSION=9.0
ARG CUDNN_VERSION=7
FROM nvidia/cuda:${CUDA_VERSION}-cudnn${CUDNN_VERSION}-devel-ubuntu16.04

#--------------------------------------------------#
#           Ubuntu dependencies                    #
#--------------------------------------------------#

# Basic Build
RUN apt update -y && apt install -y \
    git \
    bc \
    cmake \
    build-essential \
    gcc \
    g++ \
    gfortran \
    pkg-config \
    curl \
    unzip \
    tar \
    wget \
    vim \
    nano \
    ant default-jdk \
    doxygen \
    software-properties-common \
    python-dev \
    python3-dev


# Math Libraries
RUN apt update -y && apt install -y \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    liblapacke-dev \
    libeigen3-dev \
    libopencv-dev

# OpenCV Building dependencies
RUN apt update -y && apt install -y \
    ffmpeg \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libavresample-dev \
    libdc1394-22-dev \
    libtheora-dev \
    libvorbis-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk2.0-dev \
    libtiff5-dev \
    libpng12-dev \
    libjpeg-dev \
    libpng-dev \
    libjasper-dev \
    libtbb-dev \
    libtbb2 \
    qt5-default

# Caffe dependencies
RUN apt update -y && apt install -y \
    libopencv-dev \
    libgflags-dev \
    libgoogle-glog-dev \
    libhdf5-dev \
    libhdf5-serial-dev \
    liblmdb-dev \
    libleveldb-dev \
    libprotobuf-dev \
    libsnappy-dev \
    protobuf-compiler \
    libturbojpeg \
    graphviz \
    && \
    apt install -y --no-install-recommends libboost-all-dev && \
    ln -s /usr/lib/x86_64-linux-gnu/libturbojpeg.so.0.1.0 /usr/lib/x86_64-linux-gnu/libturbojpeg.so

# OpenPose dependencies
RUN apt update -y && apt install -y \
    lsof \
    apt-utils \
    lsb-core

# Misc libraries
RUN apt update -y && apt install -y \
    libffi-dev libfreetype6-dev liblcms2-dev \
    libssl-dev \
    libwebp-dev libzmq3-dev \
    zlib1g-dev libvtk6-dev \
    libwebp-dev \
    libopenexr-dev \
    libgdal-dev \
    yasm \
    libopencore-amrwb-dev \
    libv4l-dev libxine2-dev

# Link BLAS library to use OpenBLAS using the alternatives mechanism (https://www.scipy.org/scipylib/building/linux.html#debian-ubuntu)
RUN update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3

#--------------------------------------------------#
#           Clean Up                               #
#--------------------------------------------------#

# Clean up
RUN apt clean && \
    apt autoremove && \
    rm -rf /var/lib/apt/lists/*

ENV TERM=xterm-color

WORKDIR /root

