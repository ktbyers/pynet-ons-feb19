<<<<<<< HEAD
f = open("somefile.txt", "r")
print_file = f.read()
print (print_file)
f = open("newfile.txt", "w")
f.write("I like Pizza\n")
f.write("Rudy can't have pizza\n")
f.close()
f = open("newfile.txt", "a")
f.write("I had pizza for lunch\n")
=======
#!/usr/bin/env python

# READ ####
f = open("my_file.txt")
my_content = f.read()
print(my_content)

# WRITE ####
print("\nWriting file.")
f = open("new_file.txt", "w")
f.write("whatever2\n")
>>>>>>> 47e9e0b68f7c0c106c89711088f76d1b7a268ae3
f.close()
f = open("newfile.txt", "r")
print_file = f.read()
print (print_file)

