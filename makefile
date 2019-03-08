# Makefile for building docker images
default: cuda_apt_py
base: ubuntu cuda

include ubuntu/ubuntu.mk
include cuda/cuda.mk
include cuda_apt/cuda_apt.mk
include cuda_apt_py/cuda_apt_py.mk
