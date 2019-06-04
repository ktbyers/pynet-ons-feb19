#! /usr/bin/env python
ip_address = input("Please enter an IP address: ")

print("Here is the IP address: {}".format(ip_address))

ip_address = ip_address.split(".")
print(ip_address)
print(type(ip_address))

banner = '-' * 80

print(banner)
print("{:<12}{:<12}{:<12}{:<12}".format(ip_address[0], ip_address[1], ip_address[2], ip_address[3]))
print(banner)

