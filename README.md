# django_deployment

## Docker Network Commands

### List Netwroks
```
docker network ls [OPTIONS]

```
Options 

| Name          | Decription    |
| ------------- | ------------- |
| -f            | filter values (e.g. 'driver=bridge')  |
| --format      | print networks                        |
| --no-trunc    | Output without truncation             |
| -q            | Display's network IDs only            |


### Connect a running container to a network
```
docker network connect [OPTIONS] NETWORK CONTAINER
docker network connect "networkname" "containername"

```
| Name          |	Description   |
| ------------- | ------------- |
|--alias		        | Add network-scoped alias for the container|
|--driver-opt		    | driver options for the network|
|--ip		            | IPv4 address (e.g., 172.30.100.104)|
|--ip6		          | IPv6 address (e.g., 2001:db8::33)|
|--link		          | Add link to another container|
|--link-local-ip		| Add a link-local address for the container|
