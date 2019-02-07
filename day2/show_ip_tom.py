filename = "show_ip_int_brief.txt"
from pprint import pprint  # imports pretty print to python script

with open(filename) as some_var:
    show_ip_int = some_var.read()

show_ip_int = show_ip_int.strip()  # this strips whitespace

output_dict = (
    {}
)  # this creates an empty dictionary - should be done outside of for loop
for line in show_ip_int.splitlines():
    if "Interface" in line:
        continue
    fields = line.split()
    interface = fields[0]
    ip_addr = fields[1]
    line_status = fields[4]
    line_protocol = fields[5]
    output_dict[interface] = {}
    output_dict[interface]["ip_addr"] = ip_addr
    output_dict[interface]["line_status"] = line_status
    output_dict[interface]["line_protocol"] = line_protocol
    # if re.search(r"^Interface.*Protocol", line):
    # print(outiput_dict)
    # break
    # print(line)
    # break
pprint(output_dict)  # prints it pretty
