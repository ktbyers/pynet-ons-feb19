network_device = {
    'ip_address': '10.10.30.2',
    'hostname': 'cisco3.lasthop.io',
    'username': 'admin',
    'password': 'cisco123',
    'vendor': 'cisco'}
banner = '-' * 40

#Printing initial keys and values
print(banner)
print("{:^10}{:^18}".format("Keys", "Values"))
print(banner)
for k, v in network_device.items():
    print("{:10} ---> {:8}".format(k, v))
print(banner)

#Changing existing value and adding a value
network_device['password'] = 'rudyistryingtokillkyle'
network_device['secret'] = 'THISISSECRET'

network_device.get('device_type', 'Cisco_IOS')
device_type = network_device.get('device_type', 'The default device type is: Cisco_IOS')
print(device_type)

#Print off changed keys and values
print(banner)
for k, v in network_device.items():
    print("{:10} ---> {:8}".format(k, v))
print(banner)

print(network_device.get('device_type'))
