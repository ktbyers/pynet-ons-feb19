#!/usr/bin/env python
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler

def write_file(file_name, output):
    with open (file_name, "w") as f:
        f.write(output)

if __name__ == "__main__":

    password = getpass("Enter password: ")
#Cisco Show Version
    cisco1 = {
        "device_type": "cisco_ios",
        "ip": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    net_connect = ConnectHandler(**cisco1)
    show_version_cisco = net_connect.send_command("show version")
    #print(show_version_cisco)
    write_file("cisco1_ver.txt", show_version_cisco)

#Nexus Show Version
    nexus1 = {
        "device_type": "cisco_nxos",
        "ip": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }
    net_connect = ConnectHandler(**nexus1)
    show_version_nexus = net_connect.send_command("show version")
    #print(show_version_nexus)
    write_file("nexus1_ver.txt", show_version_nexus)


