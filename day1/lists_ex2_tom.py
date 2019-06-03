#!/usr/bin/env python3
from __future__ import print_function
address = ("43.43.43.43")
octet = address.split(".")
print("{:<12} {:<12} {:<12} {:<12}".format(*octet))
del octet[3]
octet.append('0')
a = bin(int(octet))
print (octet)
print (a)

