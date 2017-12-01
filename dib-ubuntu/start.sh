if [ ! -f /data/ubuntu1604.raw  ]; then
    disk-image-create ubuntu baremetal dhcp-all-interfaces bootloader -o /data/ubuntu1604.raw -t raw -x
fi
