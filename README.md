# Lithium - simplest of metals

Welcome to Lithium!

Lithium is small microservice based tool that will allow you to quickly install
base operating systems on new environments.

# Quickstart

## Requirements

Lithium requires docker and docker-compose.

## Couple notes about networking

Lithium, unlike most of bare metal deployment tools, doesn't have DHCP server. You need to setup DHCP in network. Lithium will listen on PXE requests and will respond to those.

## Start installing baremetal

To start bootstrapping your nodes all you have to do is:

```bash
export LITHIUM_IMAGE=centos7  # This is image that will be installed. Currently only centos7 and ubuntu1604 are supported
export LITHIUM_PUBKEY=$(cat ~/.ssh/id_rsa.pub)  # Pubkey for lithium user
export LITHIUM_HOST=192.168.10.1  # IP address of this node that new servers will be able to access

docker-compose up
```

And that's it, wait for dib-ubuntu and dib-centos containers to finish (building images), and next time you boot server in same network from PXE, image should be installed.

After it reboots from disk just use
```bash
ssh lithium@<<ip of machine>>
```

Images will be built only once. To rebuild fresh images run

```bash
docker-compose down --volume
docker-compose up
```

