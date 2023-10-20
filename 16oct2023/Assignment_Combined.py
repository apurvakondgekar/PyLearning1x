'''
Task #1
✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
If, elif, else
'''

score = 89
output = None

A = range(90,101)
B = range(80,90)
C = range(70,80)
D = range(60,70)
F = range(0,60)

if score in A:
    Output = "Grade is A"
elif score in B:
    Output = "Grade is B"
elif score in C:
    Output = "Grade is C"
elif score in D:
    Output = "Grade is D"
else:
    Output = "Grade is E"

print(Output)

'''
Task #2
✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year
'''

input_year = 2024
output = None

if (input_year % 4 ==0 and input_year%100 != 0) or input_year % 400 == 0:
    Output = "Leap Year"
else:
    Output = "Not a Leap Year"

print(Output)

'''
Task #3
✅ Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
'''

s1 = float(input("Enter length of s1\n"))
s2 = float(input("Enter length of s2\n"))
s3 = float(input("Enter length of s3\n"))

Output = None

if s1==s2 and s1==s3:
    Output = "Equilateral"
elif s1==s2 or s1==s3 or s2==s3:
    Output = "Isoceles"
else:
    Output = "Scalene"

print(Output)