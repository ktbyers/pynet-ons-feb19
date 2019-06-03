from __future__ import print_function
def my_func(x, y, z=20):
    return x + y + z
   
print(my_func(2, 4, 8))
print(my_func(2, 4))
print(my_func(x=3, y=5, z=7))
print(my_func("x", "y", "z"))
list = ["23"]
list2 = ["22"]
list3 = ["13"]
print(my_func(list, list2, list3))

return_val = my_func(x=["x"], y=["y"], z=["z"])
print("Calling with three lists: {}".format(return_val))
print()

#def my_func(x, y, z):
#    print(x)
#    print(y)
#    print(z)

my_list = [33, 44, 55]
my_dict = {'x': 10, 'y': 20, 'z': 30}

kwargs = my_func(**my_dict)
args = my_func(*my_list)
print("using args and list: {}".format(args))
print("Calling with **kwargs: {}".format(kwargs))


## 3rd lab

def read_file(show_version.txt):
    with open(show_version.txt) as f:
        return f.read()

def find_serial_number(show_ver):
    serial_number = ""
    for line in show_ver.splitlines():
        if "Processor board ID" in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number
