# django_deployment

## Docker Network Commands

### List Netwroks
```
docker network ls [OPTIONS]
docker network ls
```
https://docs.docker.com/engine/reference/commandline/network_ls/

### Create network
```
docker network create syntaxboard

```
https://docs.docker.com/engine/reference/commandline/network_create/

### Connect a running container to a network
```
docker network connect [OPTIONS] NETWORK CONTAINER
docker network connect "networkname" "containername"

```
https://docs.docker.com/engine/reference/commandline/network_connect/



