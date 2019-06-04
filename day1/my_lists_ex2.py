banner = '-' * 80
ip_addr = '10.1.1.1'

ip_addr = ip_addr.split(".")

print(ip_addr)

ip_addr[3] = '0'

print(ip_addr)

bin1 = bin(int(ip_addr[0]))
bin2 = bin(int(ip_addr[1]))
bin3 = bin(int(ip_addr[2]))
bin4 = bin(int(ip_addr[3]))
print(banner)
print("{:^80}".format('DECIMAL'))
print("{:^20}{:^20}{:^20}{:^20}".format(ip_addr[0], ip_addr[1], ip_addr[2], ip_addr[3]))
print(banner)
print("{:^80}".format('BINARY'))
print("{:^20}{:^20}{:^20}{:^20}".format(bin1, bin2, bin3, bin4))
print(banner)

