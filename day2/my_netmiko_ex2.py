from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

hostname = 'nxos1.lasthop.io'

nx0s1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
#    'session_log': hostname + '.txt',
}

connect = ConnectHandler(**nx0s1)
log_hist = connect.send_config_set('logging history size 200')
print(log_hist)

#for net_device in [nx0s1]:
#    connect = ConnectHandler(**nxos1)
#    log_hist = connect.send_config_set('logging history size 200')
#    print(log_hist)

with open("nx0s1_log_change.txt", "w") as f:
    f.write(log_hist)

