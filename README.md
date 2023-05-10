# **Project 1: Secure Statistics with Homomorphic Encryption**
## EPITA SRS 2024
angel.bochenko
celine-gisele.mafetgo-malego
julien.wirth
mohamed-badreddine.zouhair

## Architecture
.
├── data
│   ├── client `/data dir of client container`
│   ├── framingham_heart_disease_raw.csv `clear data`
│   └── server `/data dir of server container`
├── docker_client `client docker files`
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── docker_server `client docker files`
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run_vsftpd_and_check_if_files.sh `run ftp server and task to check for data files presence`
│   └── vsftpd.conf `ftp server poor configuration`
├── README.md `:^)`
├── run.sh `automation script to run`
├── src `python source files distributed to containers`
│   ├── client_init.py
│   ├── client_result.py
│   ├── __init__.py
│   ├── requirements.txt
│   ├── server_compute.py
│   └── utils
│       ├── __init__.py
│       └── Person.py

## Overall
Demonstration of homomorphic encryption using tenseal for Python and shell for automation.  
Scripts are meant to be used with the docker containers provided. If you run it on your host,
it will break because of paths, python dependencies, etc.  
Expected result is that statistics results made on encrypted data are the same or almost the
same as the ones made on clear data, while keeping data secret from the server.

## Requirements
docker
docker-compose

## Automatic script
`./run.sh`
It builds containers, encrypts "data/framingham_heart_disease_raw.csv" in client container,
sends encrypted file to FTP server container, the server computes means on encrypted data,
client takes the result of computation, and finally decrypts it and saves it in 
___./data/decrypted_results.csv___.  

Make sure that ___./data/client___ and ___./data/server___ are empty before running `./run.sh`
again. Otherwise, decrypted means would not be ok.

## Docker use

### Setup

``docker-compose up -d --build`` to run both FTP server and client containers.

### Run interactively

``docker exec -it {{'client' or 'server'}} sh``

### Kill running containers

``docker-compose down``

### To know

Tenseal pip package is not available on Alpine, so containers are Ubuntu based (x11 bigger...).  
Both containers are in 192.168.125.0/29 subnet.  
Server is 192.168.125.2 and client is 192.168.125.3.  
192.168.125.1 is reserved for the host's virtual bridge network interface used to manage
the network routing between the containers and the host system.

___./data/server___ on `host` is linked to ___/data___ directory from `server` container.  
___./data/client___ on `host` is linked to ___/data___ directory from `client` container.

These volumes are persistent, data in these directories won't be lost after containers shutdown.

## Misc.

### Interactive FTP transfer.
    1. Run the containers as in `Setup` part.
    2. Interactively spawn a shell in the client container.
    3. `cd /data && echo -en "test\n" > test.txt` : create a file on host and in container.
    4. `lftp -u root,toortoor 192.168.125.2` : connect to FTP server from the other container.
    5. `put text.txt` : send the file to the /data directory of the FTP server container.
