from netmiko import Netmiko
from getpass import getpass
from netmiko import ConnectHandler

def write_file(filename, show_run):
    with open(filename, "w") as f:
        f.write(show_run)

banner = '-' * 80
password = getpass()

cisco3 = {
    'device_type': 'cisco_ios',
    'host':   'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

nx0s1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
}

# SHOW PROMPT
for net_device in (cisco3, nx0s1):
    connect = ConnectHandler(**net_device)
    prompt = connect.find_prompt()
    print(prompt)

print(banner)

# SHOW VERSION
for net_device in (cisco3, nx0s1):
    connect = ConnectHandler(**net_device)
    show_ver = connect.send_command('show version')
    print(show_ver)

print(banner)

# SHOW RUN
for net_device in (cisco3, nx0s1):
    connect = ConnectHandler(**net_device)
    show_run = connect.send_command('show run')
    print(show_run)
    write_file(net_device + ".txt", show_run)

