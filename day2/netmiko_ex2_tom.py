from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler
#from ext_devices import device1, device2, device3

if __name__ = "__main__":

password = getpass("Enter password: ")
hostname = "nxos1.lasthop.io"
nexus1 = {
    "device_type": "cisco_nxos",
    "ip": hostname,
    "username": "pyclass",
    "password": password,
    "session_log": hostname + ".log",
}
net_connect = ConnectHandler(**nexus1)

config = ['logging history size 200', 'show int status']
net_connect.send_config_set(config)
net_connect.save_config
net_connect.find_prompt()
net_connect.disconnect()
nexus1 = {
    "device_type": "cisco_nxos",
    "ip": hostname,
    "username": "pyclass",
    "password": password,
    "session_log": hostname + ".log",
