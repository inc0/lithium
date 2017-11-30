FROM nginx

RUN mkdir -p /usr/share/nginx/html/pxeboot
RUN mkdir -p /usr/share/nginx/html/images
RUN mkdir -p /usr/share/nginx/html/centos/LiveOS

RUN apt-get update && apt-get -y install sudo qemu-utils wget curl python-pip

RUN curl -o /usr/share/nginx/html/pxeboot/initrd.img http://mirror.centos.org/centos/7/os/x86_64/images/pxeboot/initrd.img
RUN curl -o /usr/share/nginx/html/pxeboot/vmlinuz http://mirror.centos.org/centos/7/os/x86_64/images/pxeboot/vmlinuz
RUN curl -o /usr/share/nginx/html/centos/LiveOS/squashfs.img http://mirror.centos.org/centos/7/os/x86_64/LiveOS/squashfs.img

