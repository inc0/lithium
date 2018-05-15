FROM golang:1.9.6-stretch

RUN apt-get install git
RUN mkdir -p /go/src/zero-os/
RUN git clone https://github.com/inc0/cloud-init-server.git /go/src/zero-os/cloud-init-server \
    && cd /go/src/zero-os/cloud-init-server && go get && go build main.go && mv main /usr/local/bin/cloud-init-server

RUN mkdir -p /etc/cloud-init
EXPOSE 80
CMD cloud-init-server

