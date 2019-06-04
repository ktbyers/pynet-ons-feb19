
def read_file(filename):
    with open(filename) as f:
        return f.read()

show_ver = read_file("show_version.txt")

def find_serial_number(show_ver):
    serial_number = ""
    for line in show_ver.splitlines():
        if "Processor board ID" in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number

serial_number = find_serial_number(show_ver)
print("\nSerial Number is {}\n".format(serial_number))

