#Ternary Operator

# age > 18 then can watch a movie
# age < 18 then not allowed to watch a movie

# result_if_ture if condition else result_if_false
x = 5
y = 10

max_val = x if x>y else y
print(max_val)

age = input ("Enter your age\n")
age = int(age)

result = "Yes"  if age > 18 else "No"
print(result)