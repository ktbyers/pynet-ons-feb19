
banner = '-' * 80

with open("show_ip_bgp.txt") as f:
    show_ip_bgp = f.read()

#print(banner)
#print("Initial show ip bgp output from file")
#print()
#print(show_ip_bgp)
#print(banner)
#print(banner)

show_ip_bgp = show_ip_bgp.split("Path")
#print("Splitting show ip bgp output based on Path")
#print()
#print(show_ip_bgp)
#print(banner)

network = show_ip_bgp[1].split("*")
#print("Splitting the network data based on the *")
#print()
#print(network)
#print(banner)
#print(type(network))


#print("Listing first item in the network list")
#print()
#print(network[1])
print(banner)
print("{:^20} {:^40}".format("Network", "AS Path"))
print(banner)
for x in network[1:]:
    line = x.split()
    prefix = line[0]
    as_path = line[4:]
    as_path = ' '.join(as_path)
    print("{:20} {:40}".format(prefix, as_path))
print(banner)

