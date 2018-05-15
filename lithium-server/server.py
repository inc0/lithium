import argparse
import json
import jinja2
from flask import Flask
from flask import render_template

app = Flask(__name__)

parser = argparse.ArgumentParser(description='Boot configuration for lithium')
parser.add_argument("--image", help="Image to install. Currently suppors centos 7 and ubuntu1604", required=True)
parser.add_argument("--pubkey", help="Ssh key to include for root user", required=True)
parser.add_argument("--host-ip", help="IP address of host this application runs on", required=True)

args = parser.parse_args()

@app.route('/kickstart/<mac_address>')
def kickstart(mac_address):
    print("Writing cloud config")
    with open("/etc/cloud-init/default", "w") as f:
        user_data = {
            "meta-data": {},
            "user-data":
                {
                    "users": [
                        {
                            "name": "lithium",
                            "shell": "/bin/bash",
                            "sudo": "ALL=(ALL) NOPASSWD: ALL",
                            "ssh_authorized_keys": [args.pubkey,]
                        }
                    ]
                }
            }
        f.write(json.dumps(user_data))
    print("Serving template {}, {}, {}".format(args.image, args.pubkey, args.host_ip))
    return render_template('kickstart-simple.j2', image=args.image, pubkey=args.pubkey, host_ip=args.host_ip)


@app.route('/v1/boot/<mac_address>')
def index(mac_address):
    print(mac_address)
    with open("./macs", "a") as f:
        f.write(mac_address + " ")
    resp = {
            'kernel': 'http://{host_ip}:8010/pxeboot/vmlinuz'.format(host_ip=args.host_ip),
            'initrd': [
                'http://{host_ip}:8010/pxeboot/initrd.img'.format(host_ip=args.host_ip),
            ],
            'cmdline': 'text inst.repo=http://{host_ip}:8010/centos  ks=http://{host_ip}:8000/kickstart/{mac} cloud-config-url=http://{host_ip}:8020'.format(
                mac=mac_address,
                host_ip=args.host_ip,
                )
        }
    return json.dumps(resp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
