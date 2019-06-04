filename = "show_ip_int_brief.txt"
from pprint import pprint

with open(filename) as f:
    show_ip_int = f.read()

show_ip_int = show_ip_int.strip()

# creating a blank dictionary
output_dict = {}
for line in show_ip_int.splitlines():
    if "Interface" in line:
        continue
    fields = line.split()
    # interface, ip_addr, junk1, junk2, line_status, line_protocol = fields.split()
    interface = fields[0]
    ip_addr = fields[1]
    line_status = fields[4]
    line_protocol = fields[5]
    output_dict[interface] = {}
    output_dict[interface]["ip_addr"] = ip_addr
    output_dict[interface]["line_status"] = line_status
    output_dict[interface]["line_protocol"] = line_protocol

pprint(output_dict)


# print(show_ip_int)
