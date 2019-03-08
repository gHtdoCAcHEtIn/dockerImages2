# GPU CUDA docker images with apt updates, and python libraries

cuda_apt_py: cuda_apt_py_default
cuda_apt_py_default: cuda9_apt_py
cuda_apt_py_all: cuda8_apt_py cuda9_apt_py

## cuda 8.0
cuda8_apt_py: cuda80_apt_py
cuda80_apt_py: cuda80_apt_py2

## cuda 8.0 python2
cuda80_apt_py2: jupyter_common_files cuda80_apt
	docker build \
		-t nrca/cuda_py:cuda80.py2 \
		-f cuda_apt_py/Dockerfile \
		--rm \
		--build-arg CUDA_VERSION=cuda80 \
		--build-arg PYTHON=python \
		.

## cuda 9.0
cuda9_apt_py: cuda90_apt_py
cuda90_apt_py: cuda90_apt_py2 cuda90_apt_py3

## cuda 9.0 python2
cuda90_apt_py2: jupyter_common_files cuda90_apt
	docker build \
		-t nrca/cuda_py:cuda90.py2 \
		-f cuda_apt_py/Dockerfile \
		--rm \
		--build-arg CUDA_VERSION=cuda90 \
		--build-arg PYTHON_VERSION=2 \
		cuda_apt_py

## cuda 9.0 python3
cuda90_apt_py3: jupyter_common_files cuda90_apt
	docker build \
		-t nrca/cuda_py:cuda90.py3 \
		-f cuda_apt_py/Dockerfile \
		--rm \
		--build-arg CUDA_VERSION=cuda90 \
		--build-arg PYTHON_VERSION=3 \
		cuda_apt_py

jupyter_common_files: cuda_apt_py/jupyter_notebook_config.py cuda_apt_py/run_jupyter.sh

cuda_apt_py/jupyter_notebook_config.py: common/jupyter_notebook_config.py
	cp common/jupyter_notebook_config.py cuda_apt_py/

cuda_apt_py/run_jupyter.sh: common/run_jupyter.sh
	cp common/run_jupyter.sh cuda_apt_py/

.PHONY: cuda_apt_py/jupyter_notebook_config.py cuda_apt_py/run_jupyter.sh