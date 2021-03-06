ARG CUDA_VERSION=cuda90
ARG PY_VERSION=py3
FROM nrca/cuda_py:${CUDA_VERSION}.${PY_VERSION}

# ARG PYTHON_VERSION=3
# ARG PYTHON=python${PYTHON_VERSION}

ARG TENSORFLOW_VERSION=1.8.0
ARG TENSORFLOW_ARCH=gpu
ARG KERAS_VERSION=2.1.0
ARG CAFFE_VERSION=master
ARG NVCAFFE_VERSION="caffe-0.17"
ARG OPENCV_VERSION=3.4.0
ARG CUPY_VERSION=4.0
ARG CHAINER_VERSION=4.0

#--------------------------------------------------#
#           Tensorflow                             #
#--------------------------------------------------#

# Install TensorFlow
RUN ${PYTHON} -m pip --no-cache-dir install tensorflow-${TENSORFLOW_ARCH}~=${TENSORFLOW_VERSION}

#--------------------------------------------------#
#           Keras                                  #
#--------------------------------------------------#

# Install Keras
RUN ${PYTHON} -m pip install --no-cache-dir keras~=${KERAS_VERSION}

#--------------------------------------------------#
#           Opencv                                 #
#--------------------------------------------------#

# Currently, both CUDA=ON and build with OpenCV Contrib Modules

# Install OpenCV

# Note: -DPYTHON2_EXECUTABLE=/usr/bin/python2  was added to prevent an 
# error with some python headers during installation (opencv + python3)
# https://github.com/opencv/opencv/issues/10771#issuecomment-384951369

ARG OPENCV_CONTRIB=/root/opencv/opencv_contrib-${OPENCV_VERSION}
RUN mkdir /root/opencv
COPY opencv-${OPENCV_VERSION}.tar.gz /root/opencv/
COPY opencv_contrib-${OPENCV_VERSION}.tar.gz /root/opencv/

WORKDIR /root/opencv
RUN tar -xzf opencv-${OPENCV_VERSION}.tar.gz && \
    tar -xzf opencv_contrib-${OPENCV_VERSION}.tar.gz
WORKDIR /root/opencv/opencv-${OPENCV_VERSION}
RUN mkdir build
WORKDIR /root/opencv/opencv-${OPENCV_VERSION}/build
RUN cmake \
    -DWITH_CUDA=ON \
    -DWITH_NVCUVID=ON \
    -DCUDA_NVCC_FLAGS="-Wno-deprecated-gpu-targets" \
    -DWITH_QT=ON \
    -DWITH_OPENGL=ON \
    -DFORCE_VTK=ON \
    -DWITH_TBB=ON \
    -DWITH_OPENMP=ON \
    -DWITH_IPP=ON \
    -DBUILD_OPENCV_PYTHON=ON \
    -DBUILD_PYTHON=ON \
    -DPYTHON_EXECUTABLE="/usr/bin/${PYTHON}" \
    -DPYTHON2_EXECUTABLE="/usr/bin/python2" \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_DOCS=OFF \
    -DBUILD_TESTS=OFF \
    -DOPENCV_EXTRA_MODULES_PATH=${OPENCV_CONTRIB}/modules \
    ..
RUN make -j"$(nproc)" && \
    make install && \
    ldconfig && \
    echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc

#--------------------------------------------------#
#           BVLC/Caffe                             #
#--------------------------------------------------#

# -DCUDA_ARCH_NAME="Pascal" flag required for cuda9.0+ until Caffe starts supporting Volta architectures
# EDIT: -DCUDA_ARCH_NAME="Pascal" ==> Manual, 70, 70
#    -DCUDA_ARCH_NAME="Manual" \
#    -DCUDA_ARCH_BIN="70" \
#    -DCUDA_ARCH_PTX="70" \
# -DCUDA_NVCC_FLAGS="-Wno-deprecated-gpu-targets" \

# Install Caffe
RUN git clone -b ${CAFFE_VERSION} --depth 1 https://github.com/BVLC/caffe.git /root/caffe
#RUN git clone -b ${NVCAFFE_VERSION} --depth 1 https://github.com/NVIDIA/caffe.git /root/caffe

WORKDIR /root/caffe
RUN ${PYTHON} -m pip install -r python/requirements.txt

WORKDIR /root/caffe
RUN mkdir build

ENV PYTHON_VERSION=3

WORKDIR /root/caffe/build
RUN cmake \
    -DCPU_ONLY=OFF \
    -DUSE_CUDNN=ON \
    -DUSE_NCCL=ON \
    -DBLAS=open \
    -DBUILD_python=ON \
    -Dpython_version=${PYTHON_VERSION} \
    -DPYTHON_EXECUTABLE="/usr/bin/${PYTHON}" \
    -DBUILD_docs=OFF \
    -DCUDA_ARCH_NAME="Manual" \
    -DCUDA_ARCH_BIN="70" \
    -DCUDA_ARCH_PTX="70" \
    ..

RUN make -j"$(nproc)" all && \
    make pycaffe && \
    make install

# Set up Caffe environment variables
ENV CAFFE_ROOT=/root/caffe
ENV PYCAFFE_ROOT=$CAFFE_ROOT/python
ENV PYTHONPATH=$PYCAFFE_ROOT:$PYTHONPATH
ENV PATH=$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && \
    ldconfig

#--------------------------------------------------#
#           Chainer                                #
#--------------------------------------------------#

# Install Cupy
RUN apt install g++ && \
    ${PYTHON} -m pip install --upgrade setuptools && \
    ${PYTHON} -m pip install --no-cache-dir cupy~=${CUPY_VERSION}

# Install Chainer
RUN apt install protobuf-compiler libprotobuf-dev && \
    ${PYTHON} -m pip install "cupy>=4.0.0" "Pillow>=2.3.0" "h5py>=2.5.0" && \
    ${PYTHON} -m pip install --no-cache-dir chainer~=${CHAINER_VERSION}

# Install chainer-dashboard
RUN ${PYTHON} -m pip install --no-cache-dir https://github.com/butsugiri/chainer-dashboard/archive/0.0.1.tar.gz

#--------------------------------------------------#
#           Clean Up                               #
#--------------------------------------------------#

# Clean up
RUN apt clean && \
    apt autoremove && \
    rm -rf /var/lib/apt/lists/*

# Expose Ports for TensorBoard (6006)
EXPOSE 6006

WORKDIR "/root"
