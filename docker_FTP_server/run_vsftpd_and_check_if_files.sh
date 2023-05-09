#!/bin/bash

CONTEXT="/data/context.bin"
ENC_DATA="/data/enc_data.b64"

vsftpd /etc/vsftpd.conf &

while true
do
    if [ -f "$CONTEXT" ] && [ -f "$ENC_DATA" ]
    then
        echo "STARTING PROCESS..."
    fi
    sleep 10
done

