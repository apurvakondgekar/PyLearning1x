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