all: tf_bazel_18 tf_bazel_19 tf_bazel_110

tf_bazel_18:
	docker build -t nrca/tensorflow:1.8-devel-gpu-build -f Dockerfile --rm . --build-arg TF_VERSION=1.8.0
tf_bazel_19:
	docker build -t nrca/tensorflow:1.9-devel-gpu-build -f Dockerfile --rm . --build-arg TF_VERSION=1.9.0
tf_bazel_110:
	docker build -t nrca/tensorflow:1.10-devel-gpu-build -f Dockerfile --rm . --build-arg TF_VERSION=1.10.0

