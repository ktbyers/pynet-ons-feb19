from getpass import getpass

password = getpass("Enter standard password: ")

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

arista2 = {
    "hostname": "arista2.lasthop.io",
    "device_type": "eos",
    "username": "pyclass",
    "password": password,
    "optional_args": {},
}

srx2 = {
    "hostname": "srx2.lasthop.io",
    "device_type": "junos",
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

nxos2 = {
    "hostname": "nxos2.lasthop.io",
    "device_type": "nxos",
    "username": "pyclass",
    "password": password,
    "optional_args": {"port": 8443},
}

device_list = [cisco3, cisco4, arista1, nxos1]
