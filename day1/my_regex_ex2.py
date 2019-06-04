import re

with open("show_mac_multicast.txt") as f:
    show_mac = f.read()

#print(show_mac)

output = re.search(r"^-------.*----------------------------$", show_mac, flags=re.M)
print(output)

print(output[0])
print()

