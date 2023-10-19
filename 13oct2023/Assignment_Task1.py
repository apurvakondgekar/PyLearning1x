'''
Task 1
Explain the difference between the = operator and the == operator in Python.
What does the ** operator do in Python, and how is it used?
What does the ^ operator do in Python, and in what context is it commonly used?
'''

#Difference between = and == operators:
#= (Assignment Operator): In Python, the = operator is used for variable assignment.
#It assigns the value on the right side to the variable on the left side.

x = 10  # Assigns the value 10 to the variable x

#== (Equality Operator): The == operator is used for comparison.
# It checks if the values on both sides are equal. It returns True if they are equal and False if they are not.

a = 5
b = 5
result = (a == b)  # result will be True

# Assignment and Equality Operators
x = 10  # Assignment
y = 10  # Assignment
are_equal = (x == y)  # Equality
print("Assignment Operator:", x)
print("Equality Operator (x and y are equal):", are_equal)

#The ** Operator in Python:
#The ** operator is used for exponentiation.
# It raises the number on the left side to the power of the number on the right side.

# Exponentiation Operator
x = 2
y = 3
exponentiation_result = x ** y  # result will be 8 (2^3)
print("Exponentiation Operator (2^3):", exponentiation_result)

#The ^ Operator in Python:
#The ^ operator is the bitwise XOR operator in Python.
# It performs a bitwise exclusive OR operation on the binary representation of numbers.
# It returns 1 if the corresponding bits are different and 0 if they are the same.

# Bitwise XOR Operator
a = 5  # Binary: 101
b = 3  # Binary: 011
bitwise_xor_result = a ^ b  # result will be 6 (Binary: 110)
print("Bitwise XOR Operator (5 ^ 3):", bitwise_xor_result)

#The ^ operator can also be used for flipping individual bits.
# For example, to toggle the nth bit of a number, you can use the expression x ^ (1 << n).
