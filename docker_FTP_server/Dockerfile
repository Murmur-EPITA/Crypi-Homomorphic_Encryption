FROM alpine:latest

RUN apk add --no-cache vsftpd

COPY vsftpd.conf /etc/vsftpd/vsftpd2.conf

EXPOSE 20 21 21100-21110

RUN echo 'root:toortoor' | chpasswd
CMD ["vsftpd", "/etc/vsftpd/vsftpd2.conf"]

