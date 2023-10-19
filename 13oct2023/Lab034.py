#Identity Operators
# is Returns True if both variables are the same object
# is not Returns True if both variables are not the same object
# used with list, set, dictionaries

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)
print(x is not y)
print(id(x))
print(id(y))
# Answer is false because these are different
# as the location/reference area is different

a = 10
b = 10
#is is not used in basic int case