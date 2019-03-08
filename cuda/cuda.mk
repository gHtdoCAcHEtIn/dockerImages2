# Ubuntu (GPU) or CUDA images

cuda: cuda_default
cuda_default: cuda90cudnn7
cuda_all: cuda8 cuda9
cuda8: cuda80cudnn6
cuda9: cuda90cudnn7 cuda91cudnn7 cuda92cudnn7

cuda80cudnn6:
	docker pull nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

cuda90cudnn7:
	docker pull nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

cuda91cudnn7:
	docker pull nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

cuda92cudnn7:
	docker pull nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

# END