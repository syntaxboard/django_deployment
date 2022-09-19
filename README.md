# django_deployment

## Docker 

### List Images
```
docker image ls [OPTIONS] [REPOSITORY[:TAG]]
docker image ls
```
[Docker Image List Options](https://docs.docker.com/engine/reference/commandline/image_ls/)

### Docker Image Build
```
docker image build [OPTIONS] PATH | URL | -
docker image build -f Name of the Dockerfile (Default is 'PATH/Dockerfile')
```


### List Containers
```
docker ps [OPTIONS]
docker ps
```
[Docker Container List Options](https://docs.docker.com/engine/reference/commandline/ps/)

## Docker Network Commands

### List Networks
```
docker network ls [OPTIONS]
docker network ls
```
[Docker Network List Options](https://docs.docker.com/engine/reference/commandline/network_ls/)

### Create network
```
docker network create syntaxboard

```
[Docker Network Create Options](https://docs.docker.com/engine/reference/commandline/network_create/)

### Connect a running container to a network
```
docker network connect [OPTIONS] NETWORK CONTAINER
docker network connect "networkname" "containername"

```
[Docker Network Connect Options](https://docs.docker.com/engine/reference/commandline/network_connect/)



