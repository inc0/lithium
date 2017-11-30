FROM centos:7

RUN yum -y install sudo qemu-img wget curl e4fsprogs
RUN curl "https://bootstrap.pypa.io/get-pip.py" | python
RUN pip install diskimage-builder
COPY start.sh /
RUN chmod +x /start.sh
CMD /start.sh

