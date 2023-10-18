#String Functions
# Python Immutable in Nature

name = 'sarthi'
# name = 'dutta' will only replace the variable name

#capitalize()
#Returns a copy of the string with its first character capitalised
result = name.capitalize()
print(result)
print(name)

print(id(name))
print(id(result))

# Upper case
result2 = name.upper()
print(result2)

#Lower case
result3 = name.lower()
print(result3)
print(id(result3)) # Identity reference

#Swapcase()
#Returns a copy of the string with uppercase characters converted to lowercase
# and vice versa

name = "LinkedIn"
print(name.swapcase())

#Title
# Returns a titlecases version of string
# Eg. 'Hello World'

name = "hello world"
print(name.title())

t1 = 'cat fish'
t2 = 'star fish'
print(t1.capitalize())
print(t2.upper())

#Replace
text = "hello world"
result_rep = text.replace("world","Python")
print(result_rep)

#index and len

# find()
# Returns the lowest index of a substring in the string
# Returns -1 if the substring is not found

text = "hello world"
index = text.find("world")
print(index)

# count
count = text.count("l")
print(count)

name = "p d"
print(len(name))
