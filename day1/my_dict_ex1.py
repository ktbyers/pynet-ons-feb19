
net_device = {'ip_addr': '10.1.1.1', 'username': 'admin', 'password': 'admin123', 'vendor': 'Cisco', 'model': '6807'}
banner = '-' * 40

print(banner)
print("{:20} {:20}".format("KEY", "VALUE"))
print(banner)
for key, value in net_device.items():
    print("{:20} {:20}".format(key, value))
print(banner)

net_device['password'] = 'pass123'

net_device['secret'] = 'secret123'

device_type = net_device.get("device_type", "cisco_ios")
print("\nDefault device type: {}\n".format(device_type))

