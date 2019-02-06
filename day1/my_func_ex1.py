
def my_func(x,y,z=20):
    return x + y + z

my_func(2, 3, 4)

print(my_func(x=10, y=20))

print(my_func(5, y=10, z=25))

print(my_func("X", "Y", "Z"))

list1 = ['first', 'second', 'third']
list2 = [1, 2, 3]
list3 = ['uno', 'dos', 'tres']

print(my_func(list1, list2, list3))

