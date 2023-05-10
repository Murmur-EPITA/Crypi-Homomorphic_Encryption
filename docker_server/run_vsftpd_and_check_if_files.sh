#!/bin/bash

CONTEXT="/data/pubContext.bin"
ENC_DATA="/data/enc_data.b64"

vsftpd /etc/vsftpd.conf &

while true
do
    if [ -f "$CONTEXT" ] && [ -f "$ENC_DATA" ] && [ ! -f "/data/results/mean_enc_data.b64" ]
    then
        # STARTING PROCESS...
        python3 /python_src/server_compute.py /data/pubContext.bin /data/enc_data.b64
    fi
    sleep 10
done
