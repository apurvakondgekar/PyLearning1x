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
