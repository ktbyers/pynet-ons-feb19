#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username="pyclass",
    password=password,
    optional_args={},
)

arista1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=password,
    optional_args={},
)

srx2 = dict(
    hostname="srx2.lasthop.io",
    device_type="junos",
    username="pyclass",
    password=password,
    optional_args={},
)

nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username="pyclass",
    password=password,
    optional_args={"nxos_protocol": "https", "port": 8443},
)

devices = (cisco3, arista1, srx2, nxos1)
for a_device in devices:
    device_type = a_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**a_device)

    print()
    print("\n\n>>>Test device open")
    device.open()

    print()
    banner = " Facts {} ".format(device_type)
    print(banner.center(80, "-"))
    pprint(device.get_facts())
    print("-" * 80)
    print()
