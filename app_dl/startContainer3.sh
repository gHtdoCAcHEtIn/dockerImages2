#!/bin/bash

# docker image
IMAGE=nrca/dl:cuda90.py3

# name of container
DATE=$(date +%N)
NAME=dl-cuda90-py3
CONTAINERNAME=$NAME-$DATE

# volumes to be mounted
VOLUME=/data

# other environment variables
TERM=xterm-color
PYTHONPATH=/data/projects/tf-models/research:/data/projects/tf-models/research/slim:/root/caffe/python

# ports to be mapped
#PORTS='-p 8888:8888 -p 6006:6006'
PORTS=''

# display devices
#DISPLAY='--env DISPLAY=unix$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix'
DISPLAY=''

# camera devices
#CAMERA='--device /dev/video0:/dev/video0'
CAMERA=''

nvidia-docker run \
    --interactive \
    --rm \
    --detach \
    --name $CONTAINERNAME \
    --volume $VOLUME:$VOLUME \
    --env TERM=$TERM \
    --env PYTHONPATH=$PYTHONPATH \
    $CAMERA \
    $DISPLAY \
    $PORTS \
    $IMAGE

