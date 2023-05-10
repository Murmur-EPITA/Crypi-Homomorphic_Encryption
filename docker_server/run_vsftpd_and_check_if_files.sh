#!/bin/bash

CONTEXT="/data/pubContext.bin"
ENC_DATA="/data/enc_data.b64"
computed=false

vsftpd /etc/vsftpd.conf &

while true
do
    if [ -f "$CONTEXT" ] && [ -f "$ENC_DATA" ] && !"$computed"
    then
        # STARTING PROCESS...
        python3 /python_src/server_compute.py /data/pubContext.bin /data/enc_data.b64
        computed=true
    fi
    sleep 10
done
