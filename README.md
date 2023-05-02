# cryptoProjet

## Requirements
docker
docker-compose

## Docker use

### Setup

``docker-compose up -d --build`` to run both FTP server and client containers.

### To run interactively

``docker exec -it {{client or server}} sh``

### To kill running containers

``docker-compose down``

### To know

./volumes/server on host is linked to /data directory from server container.
./volumes/client on host is linked to /data directory from client container.

These volumes are persistent, data in these directories won't be lost after containers shutdown.

## Misc.

### Interactive FTP transfer.
    - Run the containers as in ``Setup`` part.
    - Interactively spawn a shell in the client container.
    - ``cd /data && echo -en "test\n" > test.txt`` : create a file on host and in container.
    - ``lftp -u root,toortoor 192.168.125.2`` : connect to FTP server from the other container.
    - ``put text.txt`` : send the file to the /data directory of the FTP server container.
