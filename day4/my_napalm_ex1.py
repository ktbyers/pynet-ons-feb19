from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "device_type": "ios",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

cisco4 = {
    "hostname": "cisco4.lasthop.io",
    "device_type": "ios",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

arista1 = {
    "hostname": "arista1.lasthop.io",
    "device_type": "eos",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

nxos1 = {
    "hostname": "nxos1.lasthop.io",
    "device_type": "nxos",
    "username": "pyclass",
    "password": password,
    "optional_args": {"port": 8443},
}

devices = [cisco3, cisco4, arista1, nxos1]

banner = '-' * 80

for device in devices:
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**device)
    print()
    print("\n\n>>>Test device open")
    device.open()

    print()
    output = device.get_facts()
    #pprint(output)
    #print()
    print("Device: {hostname}".format(**output))
    print("Model: {model}".format(**output))
    print(banner)

