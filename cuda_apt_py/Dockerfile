ARG CUDA_VERSION=cuda90
FROM nrca/cuda:${CUDA_VERSION}

ARG PYTHON_VERSION=2
ENV PYTHON=python${PYTHON_VERSION}

#--------------------------------------------------#
#           Python dependencies                    #
#--------------------------------------------------#

# Install pip
RUN mkdir /root/pip && \
    cd /root/pip && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    ${PYTHON} get-pip.py && \
    rm get-pip.py

# Add SNI support to Python
RUN ${PYTHON} -m pip --no-cache-dir install \
        pyopenssl \
        ndg-httpsclient \
        pyasn1

# Install useful Python packages using apt to avoid version incompatibilities with Tensorflow binary
# especially numpy, scipy, skimage and sklearn (see https://github.com/tensorflow/tensorflow/issues/2034)
RUN apt update -y && apt install -y python-dev python3-dev python-tk python3-tk

# Install other useful Python packages using pip
RUN ${PYTHON} -m pip install --upgrade --ignore-installed --no-cache-dir ipython
RUN ${PYTHON} -m pip --no-cache-dir install \
        path.py \
        wheel \
        Cython \
        numpy \
        nose \
        h5py \
        Pillow \
        sphinx \
        pygments \
        pylint \
        zmq \
        protobuf \
        pytest \
        scipy \
        scikit-image \
        scikit-learn \
        matplotlib \
        ipykernel \
        jupyter \
        opencv-python \
        pandas \
        && \
    ${PYTHON} -m ipykernel.kernelspec

RUN ${PYTHON} -m pip --no-cache-dir install \
        imgaug \
        imageio \
        tqdm

# Set up notebook config
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly: https://github.com/ipython/ipython/issues/7062
COPY run_jupyter.sh /root/
RUN chmod u+x /root/run_jupyter.sh

# Expose Ports for Ipython (8888)
EXPOSE 8888

WORKDIR "/root"
