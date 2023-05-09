#!/bin/sh
set -e

FILENAME="framingham_heart_disease_raw.csv"

SERVER_IP="192.168.125.2"
USER="root"
PASS="toortoor"
LOCALFILEPATH="./data/$FILENAME"
REMOTEFILEPATH="/data/$FILENAME"
FTP_CLIENT_CONTAINER="client"
CLIENTVOLUME="./data/client"
SERVERVOLUME="./data/server"

# Check if data file exists in ./data directory.
[ ! -f "$LOCALFILEPATH" ] && echo "Missing $LOCALFILEPATH file. Aborting." && exit 1

[ ! -d "$VOLUMES" ] && mkdir -m 777 -p "$CLIENTVOLUME" && mkdir -m 777 -p "$SERVERVOLUME"

if [ -r "$LOCALFILEPATH" ]; then
    # Copy data file into client's volume shared with host.
    cp $LOCALFILEPATH $CLIENTVOLUME
else
    echo "Need read permission on $LOCALFILEPATH. Aborting."
    exit 1
fi

# Start the containers.
docker-compose up -d

# Send data file from client to server through FTP.
docker exec $FTP_CLIENT_CONTAINER lftp -c "open $SERVER_IP; user $USER $PASS; put $REMOTEFILEPATH"

# Shutdown the containers.
docker-compose down

# Compare statistics results between clear data and encrypted data.
if diff "$CLIENTVOLUME" "$SERVERVOLUME" >/dev/null ; then
    echo -en "\nStatistics results between clear and encrypted data are identical."
else
    echo -en "\nStatistics results between clear and encrypted data are different."
fi
