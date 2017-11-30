FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install dnsmasq syslinux wget
COPY dnsmasq.conf /etc/dnsmasq.conf
CMD dnsmasq -d

