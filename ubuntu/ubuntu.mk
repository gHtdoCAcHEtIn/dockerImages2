# Ubuntu (CPU) images

ubuntu: ubuntu_default
ubuntu_default: ubuntu16
ubuntu_all: ubuntu16 ubuntu18

ubuntu16:
	docker pull ubuntu:16.04

ubuntu18:
	docker pull ubuntu:18.04

# END
