FROM nginx

RUN mkdir /usr/share/nginx/html/pxeboot
COPY initrd.img /usr/share/nginx/html/pxeboot
COPY vmlinuz /usr/share/nginx/html/pxeboot

RUN apt-get update && apt-get -y install sudo qemu-utils wget curl python-pip

RUN mkdir /usr/share/nginx/html/images
ADD LiveOS /usr/share/nginx/html/centos/LiveOS


