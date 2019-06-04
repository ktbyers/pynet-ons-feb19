banner = '-' * 80
my_list = ['string1', 'string2', 'string3', 'string4', 'string5']

print(banner)
print("Here is the original list: \n {} {} {} {} {}".format(*my_list))
print(banner)

print("Adding 2 strings to the list")
my_list.append('string6')
my_list.append('string7')
print(my_list)
print(banner)

my_list.pop(0)
print(my_list)

print(banner)
print("Length = {}".format(len(my_list)))
print(banner)

print(my_list.sort())


