FROM ubuntu

COPY requirements.txt /

RUN apt-get update && \
    apt-get install -y vsftpd python3 python3-pip && \
        pip3 install --no-cache-dir -r /requirements.txt && \
            apt-get clean && rm -rf /var/lib/apt/lists/*

COPY vsftpd.conf /etc/vsftpd.conf
COPY run_vsftpd_and_check_if_files.sh /

EXPOSE 20 21 21100-21110

RUN echo "root:toortoor" | chpasswd
CMD bash /run_vsftpd_and_check_if_files.sh

