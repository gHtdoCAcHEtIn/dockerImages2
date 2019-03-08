ARG TF_VERSION=1.8.0
FROM tensorflow/tensorflow:${TF_VERSION}-devel-gpu

MAINTAINER Ripul Bhutani <rbhutani@nikonrca.com>


#--------------------------------------------------#
#           Bazel Build 'label_image'              #
#--------------------------------------------------#

WORKDIR /tensorflow
RUN bazel build --config=cuda tensorflow/examples/label_image/...

WORKDIR /

