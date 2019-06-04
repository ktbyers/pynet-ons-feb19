
def my_func(x,y,z=20):
    return x + y + z

list1 = ['first ', 'second ', 'third ']

print(my_func(*list1))

my_dict = {
    'x': 'value1',
    'y': 'value2',
    'z': 'value3',
}

print(my_func(**my_dict))

