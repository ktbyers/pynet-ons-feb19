import re

with open("show_int_fa4.txt") as f:
    output = f.read()

packets_in = re.search(r"(\d+) packets input, (\d+) bytes", output)
packets_out = re.search(r"(\d+) packets output, (\d+) bytes", output)
print(packets_in.group(0))
print(packets_out.group(0))
