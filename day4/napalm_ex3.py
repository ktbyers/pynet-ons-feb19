#!/usr/bin/env python
from __future__ import print_function

from napalm import get_network_driver
from my_devices_na import cisco4

if __name__ == "__main__":

    merge_files = {"cisco": "cisco_merge.txt"}

    device_type = cisco4.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**cisco4)

    if device_type == "ios":
        filename = merge_files["cisco"]
    elif device_type == "junos":
        filename = merge_files["juniper"]
    else:
        raise ValueError("Invalid device_type specified")

    print()
    print(">>>Device open")
    device.open()

    print()
    print(">>>Load config change (merge) - no commit")
    device.load_merge_candidate(filename=filename)
    print(device.compare_config())

    print()
    print(">>>Discard config change (merge)")
    device.discard_config()
    print(device.compare_config())

    print()
    print(">>>Load config change (merge) - commit")
    device.load_merge_candidate(filename=filename)
    print(device.compare_config())
    device.commit_config()

    print()
