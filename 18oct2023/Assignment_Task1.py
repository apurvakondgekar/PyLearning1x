"""
The Fibonacci series is a sequence of numbers in which each number (Fibonacci number) is the sum
 of the two preceding ones, usually starting with 0 and 1.
 In mathematical terms, the Fibonacci sequence is defined by the recurrence relation:

F(n)=F(n−1)+F(n−2)

with initial conditions:

F(0)=0,F(1)=1

So, the sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

Each number in the Fibonacci sequence (after the first two) is the sum of the two preceding numbers. This pattern
continues indefinitely, producing an infinite sequence of numbers.
The Fibonacci sequence has various applications in mathematics, computer science, and nature,
and it often appears in algorithms and problem-solving contexts.
"""
num = int(input("Enter the number"))
a = 0
b = 1

while (a < num):
    print(a,end=' ')
    a, b = b, a+b

"""
The factorial series refers to the sequence of factorials for consecutive natural numbers. 
The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers 
up to and including n. Mathematically, it is defined as:
n!=n×(n−1)×(n−2)×…×3×2×1 with the special case that 0!=1.

For example:
5!=5×4×3×2×1=120
4!=4×3×2×1=24
3!=3×2×1=6
2!=2×1=2
1!=1
0!=1
The factorial series is used in various mathematical and computational contexts, such as 
combinatorics, probability, and algorithms. 
It grows rapidly as the input number increases due to the multiplication of consecutive integers.
"""

n = int(input("\n8Enter the number"))
if n < 0 :
    print(" Factorial is not possible")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i


print("Fact is", fact)