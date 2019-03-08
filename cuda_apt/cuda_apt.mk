# GPU CUDA docker images with apt updates

cuda_apt: cuda_apt_default
cuda_apt_default: cuda9_apt
cuda_apt_all: cuda8_apt cuda9_apt
cuda8_apt: cuda80_apt
cuda9_apt: cuda90_apt

BUILDCONTEXT=cuda_apt

cuda80_apt: cuda80cudnn6
	docker build \
		-t nrca/cuda:cuda80 \
		-f cuda_apt/Dockerfile \
		--rm \
		--build-arg CUDA_VERSION=8.0 \
		--build-arg CUDNN_VERSION=6 \
		cuda_apt

cuda90_apt: cuda90cudnn7
	docker build \
		-t nrca/cuda:cuda90 \
		-f cuda_apt/Dockerfile \
		--rm \
		--build-arg CUDA_VERSION=9.0 \
		--build-arg CUDNN_VERSION=7 \
		cuda_apt
