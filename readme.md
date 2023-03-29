# Docker commands

This repository contains some Docker commands that developers can use in his daily job with this tool

### docker images

show all docker images in your host

### docker pull [IMAGE_NAME]

is responsible for downloading the image found in Docker Hub to the host

### docker run <image_name>

creates and run a container with an image, even if that image is not stored on your host

### docker run -d -P <image_name>

creates and run a container and show the ports available

### docker run -d -p [HOST_PORT:CONTAINER_PORT] <image_name>

creates and run a container and maps the specified host port to the specified container port

### docker stop [CONTAINER_ID]

stop a container passing his id

### docker start [CONTAINER_ID]

starts a container passing his id

### docker pause [CONTAINER_ID]

pause a container passing his id

### docker unpause [CONTAINER_ID]

unpause a container passing his id

### docker stop [OPTIONS] container [CONTAINER_NAME]

stops a container with some options if necessary

### docker stop [OPTIONS] container [CONTAINER_NAME or CONTAINER_ID]

stops a container with some options if necessary

### docker exec -it [CONTAINER_ID] [SOME_COMMAND]

executes a command in a container

### docker ps

show running containers

### docker ps -a

show all containers, including those that are stopped,

### docker ps -s

show all containers with his size

### docker rm [CONTAINER_ID] --force

stop and removes a container by id

### docker container rm $(docker container ls -aq)

remove all containers, including those that are stopped, by ids

### docker container rmi [IMAGE_ID]

remove an image by id

### docker container rmi $(docker container ls -aq)

remove all images by ids

### docker build -t [IMAGE_NAME] [FILE_DIRECTORY]

creates a docker image from the files of a directory

### docker history <image_name>

show image layers