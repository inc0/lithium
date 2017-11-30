import argparse
import json
import jinja2
from flask import Flask
from flask import render_template

app = Flask(__name__)

parser = argparse.ArgumentParser(description='Boot configuration for lithium')
parser.add_argument("--image", help="Image to install. Currently suppors centos 7 and ubuntu1604", required=True)
parser.add_argument("--pubkey", help="Ssh key to include for root user", required=True)
parser.add_argument("--root-pwd", help="Setup with root password")

args = parser.parse_args()

@app.route('/kickstart/<mac_address>')
def kickstart(mac_address):
    return render_template('kickstart-simple.j2', image=args.image, pubkey=args.pubkey, root_pwd=args.root_pwd)


@app.route('/v1/boot/<mac_address>')
def index(mac_address):
    print(mac_address)
    resp = {
            'kernel': 'http://192.168.10.1:8010/pxeboot/vmlinuz',
            'initrd': [
                'http://192.168.10.1:8010/pxeboot/initrd.img',
            ],
            'cmdline': 'text inst.repo=http://192.168.10.1:8010/centos  ks=http://192.168.10.1:8000/kickstart/{}'.format(
                mac_address)
        }
    return json.dumps(resp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
