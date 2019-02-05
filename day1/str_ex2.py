#Strings Ex2
#!/usr/bin/env python3
from __future__ import print_function
address = input("Enter an IP Address ")
#print (address) #used to test the input variable
address = address.split(".")
print("{:<12} {:<12} {:<12} {:<12}".format(*address))

#Create a python script that prompts for an IP address.
#Use #! at top of file; make executable
#split on ‘.’      
#Print out four octets with column width of 12; left aligned.
#Check your code into github

