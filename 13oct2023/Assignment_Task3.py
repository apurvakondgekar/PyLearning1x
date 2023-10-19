# 1. Use the ternary operator to find the maximum of three numbers entered by the user.

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = int(input("Enter third number\n"))

max_value = a if (a>b and a>c) else (b if b>c else c)
print(max_value)

# 2.Develop a Python script that calculates the square and cube of a given number.

n = int(input("Enter the number\n"))
sqr = n**
cube = n**3
print("sqr", sqr)
print("cube", cube)