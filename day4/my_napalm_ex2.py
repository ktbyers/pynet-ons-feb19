from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "device_type": "nxos",
    "username": "pyclass",
    "password": password,
    "optional_args": {"port": 8443},
}

nxos2 = {
    "hostname": "nxos2.lasthop.io",
    "device_type": "nxos",
    "username": "pyclass",
    "password": password,
    "optional_args": {"port": 8443},
}

banner = '-' * 80

for devices in [nxos1, nxos2]:
    device_type = devices.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**devices)
    print()
    print("\n\n>>>Test device open")
    device.open()
    lldp = device.get_lldp_neighbors()
    print()
    print("Device: {hostname}".format(**devices))
    print()
    pprint(lldp)
    print(banner)
    print()
