all: cuda9

## cuda 9.0 python2
cuda90py2:	
	docker build -t nrca/tensorrt-tf:cuda90.py2 -f Dockerfile.gpu.cuda9.py2 --rm --build-arg CUDA_VERSION=9.0 --build-arg PYTHON=python .

# cuda9
cuda90:	cuda90py2
cuda9: cuda90
