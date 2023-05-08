FROM alpine:latest

RUN apk add --no-cache vsftpd

COPY vsftpd.conf /etc/vsftpd/vsftpd2.conf
COPY run_vsftpd_and_check_if_files.sh /

EXPOSE 20 21 21100-21110

RUN echo "root:toortoor" | chpasswd
CMD sh /run_vsftpd_and_check_if_files.sh

