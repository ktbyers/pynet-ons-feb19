#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
from pyeapi.eapilib import CommandError
import re

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def hit_enter():
    try:
        raw_input("Hit enter to continue: ")
    except NameError:
        input("Hit enter to continue: ")


def wrapper_func(napalm_obj, napalm_method, banner=""):
    my_method = getattr(napalm_obj, napalm_method)
    print()
    print(banner.center(80, "-"))
    pprint(my_method())
    print("-" * 80)
    print()


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
napalm_conns = []
for a_device in devices:
    device_type = a_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**a_device)
    napalm_conns.append(device)

    print()
    print("\n\n>>>Test device open")
    device.open()

    print()
    banner = " Facts {} ".format(device_type)
    print(banner.center(80, "-"))
    pprint(device.get_facts())
    print("-" * 80)
    print()
hit_enter()

test_methods = [
    "get_arp_table",
    "get_mac_address_table",
    "get_interfaces",
    "get_interfaces_ip",
    "get_lldp_neighbors",
    "get_lldp_neighbors_detail",
    "get_bgp_neighbors",
    "get_users",
    "get_config",
    # "get_environment",
    # "get_snmp_information",
    # "get_bgp_neighbors_detail",
    # "get_bgp_config",
    # "get_ntp_servers",
    # "get_ntp_peers",
    # "get_ntp_stats",
    # "get_optics",
]


for napalm_method in test_methods:
    print("\n\n\n>>>Test {}".format(napalm_method))
    for conn in napalm_conns:
        # Get napalm platform name
        match = re.search(r".*napalm_(.*?)\..*", str(conn.__class__))
        device_type = match.group(1)
        banner = " {} ({}) ".format(napalm_method, device_type)
        try:
            # Executes conn.napalm_method()
            wrapper_func(conn, napalm_method, banner=banner)
        except NotImplementedError:
            print("Not implemented.")
        except CommandError:
            print("Arista exception.")
    hit_enter()
