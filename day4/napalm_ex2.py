#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint as pp

from napalm import get_network_driver
from my_devices_na import nxos1, nxos2

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    for a_device in (nxos1, nxos2):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print()
        print(">>>Device open")
        device.open()

        print("-" * 50)
        lldp = device.get_lldp_neighbors()
        pp(lldp)
    print()


if __name__ == "__main__":
    main()
