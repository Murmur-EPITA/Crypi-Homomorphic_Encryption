# **cryptoProjet**

## Requirements
docker
docker-compose

## Docker use

### Setup

``docker-compose up -d --build`` to run both FTP server and client containers.

### Run interactively

``docker exec -it {{'client' or 'server'}} sh``

### Kill running containers

``docker-compose down``

### To know

Both containers are in 192.168.125.0/29 subnet.  
Server is 192.168.125.2 and client is 192.168.125.3.  
192.168.125.1 is reserved for the host's virtual bridge network interface used to manage
the network routing between the containers and the host system.

___./volumes/server___ on `host` is linked to ___/data___ directory from `server` container.  
___./volumes/client___ on `host` is linked to ___/data___ directory from `client` container.

These volumes are persistent, data in these directories won't be lost after containers shutdown.

## Misc.

### Interactive FTP transfer.
    - Run the containers as in `Setup` part.
    - Interactively spawn a shell in the client container.
    - `cd /data && echo -en "test\n" > test.txt` : create a file on host and in container.
    - `lftp -u root,toortoor 192.168.125.2` : connect to FTP server from the other container.
    - `put text.txt` : send the file to the /data directory of the FTP server container.
