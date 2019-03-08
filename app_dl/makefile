app_dl_default: cuda90py2 cuda90py3
app_dl_all: cuda90py2 cuda90py3

## cuda 8.0
cuda80py2:
	docker build \
		-t nrca/dl:cuda80.py2 \
		-f Dockerfile.gpu.cuda8 \
		--rm \
		--build-arg CUDA_VERSION=cuda80\
		--build-arg PYTHON=python \
	.

## cuda 9.0
cuda90py2:	
	docker build \
		-t nrca/dl:cuda90.py2 \
		-f Dockerfile.gpu.cuda9.py2 \
		--rm \
		--build-arg CUDA_VERSION=cuda90 \
		--build-arg PY_VERSION=py2 \
	.

cuda90py3:
	docker build \
		-t nrca/dl:cuda90.py3 \
		-f Dockerfile.gpu.cuda9.py3 \
		--rm \
		--build-arg CUDA_VERSION=cuda90 \
		--build-arg PY_VERSION=py3 \
	.

