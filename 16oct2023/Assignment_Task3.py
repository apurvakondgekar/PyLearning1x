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