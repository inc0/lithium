if [ ! -f /data/centos7.raw ]; then
    disk-image-create centos7 baremetal dhcp-all-interfaces bootloader -o /data/centos7.raw -t raw -x
fi
