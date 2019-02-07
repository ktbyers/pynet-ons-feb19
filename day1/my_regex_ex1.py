import re

with open("show_int_fa4.txt") as f:
    show_int = f.read()

input = re.search(r"(\d+) packets input, (\d+) bytes", show_int)
output = re.search(r"(\d+) packets output, (\d+) bytes", show_int)

packets_input = input.group(1)
bytes_input = input.group(2)

packets_output = output.group(1)
bytes_output = output.group(2)

#print(packets_input)
#print(bytes_input)

print("Packet input: {} Bytes input: {}".format(packets_input, bytes_input))

print("Packet output: {} Bytes output: {}".format(packets_output, bytes_output))

