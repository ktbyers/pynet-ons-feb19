filename = "show_ip_bgp.txt"

with open(filename, "r") as f:
    bgp_table = f.read()
    
fields = bgp_table.split("Weight Path")
bgp_table = fields[1]

for line in bgp_table.splitlines():
    if not line.strip():
        continue
    fields = line.split()
    prefix = fields[1]
    as_path = fields[5:-1]
    as_path = " ".join(as_path)
    print("{:30}{:30}".format(prefix, str(as_path)))
