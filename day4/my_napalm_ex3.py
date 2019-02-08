from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

password = getpass()
filename = "my_napalm_ex3_merge.txt"

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "device_type": "ios",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

device_type = cisco3.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**cisco3)

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
