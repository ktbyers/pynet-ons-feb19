#!/usr/bin/env python
from __future__ import print_function

from napalm import get_network_driver
from my_devices_na import device_list

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    for a_device in device_list:
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print()
        print(">>>Device open")
        device.open()

        print("-" * 50)
        device_facts = device.get_facts()
        print("{hostname}: Model={model}".format(**device_facts))

    print


if __name__ == "__main__":
    main()
