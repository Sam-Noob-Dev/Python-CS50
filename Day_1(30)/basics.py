# Variables , input and output, f string, string methods 

# Input with numbers or float is diffrent
name = input("Enter your Name : ").strip().title()
age = int(input("Enter your age : "))
marks = float(input("Enter your marks : "))

# String methods 
"""
to use this methods many ways are there
eg 
name=name.strip().title()      1st way  you can apply two methods at same time also it will impact from left to right

name = input("Enter your name : ").strip().title()     2nd this way as it use less line of code we can use any of the way

.strip() - so basically it will just remove the space from the start and end if you placed 
eg 
input -:        Sam     
output -:Sam
becuse we used the strip

.captilize() - now it will just captial the first letter of the name
eg 
input - : sam kumar
output - : Sam kumar
issue is  this it will not captilize the secode one 

.title() - now it solve the issue of captilaize by putting upper first leeter of  each senetence

eg 
input - : Sam kumar
output -:Sam Kumar 

*** so the big one will stay big it will not convert itself ***
"""


# F strings and print way
print("Hello , "+name)
print(f"Your name is {name}")
print(f"Your age is {age}")
print(f"Your age is {marks}")
 

