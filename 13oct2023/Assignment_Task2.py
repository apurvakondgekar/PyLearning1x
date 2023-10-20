# 1. Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

r = float(input("Enter the radius of circle in cms\n"))
pi = 3.14

area = pi * (r**2)
#can use math.pi also instead of pi
print(area, "cm sq")

# 2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))

output = "a>b" if a>b else ("a=b" if a==b else "a<b")
print(output)