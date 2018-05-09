FROM ubuntu:16.04

RUN apt-get update && apt-get -y install sudo qemu-utils wget curl python kpartx
RUN curl "https://bootstrap.pypa.io/get-pip.py" | python
RUN pip install diskimage-builder
COPY start.sh /
RUN chmod +x /start.sh
CMD /start.sh

