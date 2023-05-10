#!/bin/sh

FILENAME="framingham_heart_disease_raw.csv"

SERVER_IP="192.168.125.2"
USER="root"
PASS="toortoor"
LOCALFILEPATH="./data/$FILENAME"
CLIENTDATAFILEPATH="/data/cipher/enc_data.b64"
CLIENTPUBCONTEXTFILEPATH="/data/keys/pubContext.bin"
CLIENTPRIVCONTEXTFILEPATH="/data/keys/privContext.bin"
SERVERRESULTFILEPATH="/data/results/mean_enc_data.b64"
RESULTFILEPATH="/results/mean_enc_data.b64"
FTP_CLIENT_CONTAINER="client"
FTP_SERVER_CONTAINER="server"
CLIENTVOLUME="./data/client"
SERVERVOLUME="./data/server"
PYTHONSOURCEDIR="./src"

# Check if data file exists in ./data directory.
[ ! -f "$LOCALFILEPATH" ] && echo "Missing $LOCALFILEPATH file. Aborting." && exit 1
[ ! -d "$PYTHONSOURCEDIR" ] && echo "Missing $PYTHONSOURCEDIR dir. Aborting." && exit 1
[ ! -d "$VOLUMES" ] && mkdir -m 777 -p "$CLIENTVOLUME" && mkdir -m 777 -p "$SERVERVOLUME"

if [ -r "$LOCALFILEPATH" ]; then
    # Copy data file into client's volume shared with host.
    cp $LOCALFILEPATH $CLIENTVOLUME
else
    echo "Need read permission on $LOCALFILEPATH. Aborting."
    exit 1
fi

# Start the containers.
docker-compose up -d --build

# Encrypt data on client
echo "\nEncrypting data in client container..."
docker exec $FTP_CLIENT_CONTAINER python3 /python_src/client_init.py
echo "OK"

# Send data file and public context from client to server through FTP.
echo "Send encrypted data from client to server..."
docker exec $FTP_CLIENT_CONTAINER lftp -c "open $SERVER_IP; user $USER $PASS; put $CLIENTDATAFILEPATH $CLIENTPUBCONTEXTFILEPATH"
echo "OK"

# Compute stats on ciphered data on server
# It does it automatically when necessary files are present: 
# see docker_server/run_vsftpd_and_check_if_files.sh

# Client get the results
# Loop until server has created results file.
echo "Waiting for the server to compute statistics on encrypted data..."
computationIsOver=false
while ! $computationIsOver
do
    docker exec $FTP_SERVER_CONTAINER test -f "$SERVERRESULTFILEPATH"
    if [ $? -eq 0 ]; then
        computationIsOver=true
        echo "OK"
    fi
    sleep 2
done
# Client can get the results file
echo "Client gets results file..."

docker exec $FTP_CLIENT_CONTAINER lftp -c "open $SERVER_IP; user $USER $PASS; get $RESULTFILEPATH"
docker exec $FTP_CLIENT_CONTAINER mkdir -p /data/results
docker exec $FTP_CLIENT_CONTAINER mv /mean_enc_data.b64 /data/results/
echo "OK"

# Client decrypt results file
echo "Client decrypts results file..."
docker exec $FTP_CLIENT_CONTAINER python3 /python_src/client_result.py $CLIENTPRIVCONTEXTFILEPATH /mean_enc_data.b64
echo "OK"

if [ "$1" != "--stay-up" ]; then
    # Shutdown the containers.
    echo "Shutting down containers..."
    docker-compose down
    echo "OK"
else
    echo "Containers are still running. Read README.md if you want to stop them."
fi

# Compare statistics results between clear data and encrypted data.
if diff "$CLIENTVOLUME" "$SERVERVOLUME" >/dev/null ; then
    echo -en "\nStatistics results between clear and encrypted data are identical."
else
    echo -en "\nStatistics results between clear and encrypted data are different."
fi
