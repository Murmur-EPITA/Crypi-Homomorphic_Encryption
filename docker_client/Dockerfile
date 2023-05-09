FROM ubuntu

COPY requirements.txt /

RUN apt-get update && \
    apt-get install -y lftp python3 python3-pip && \
        pip3 install --no-cache-dir -r /requirements.txt

CMD ["tail", "-f", "/dev/null"]
