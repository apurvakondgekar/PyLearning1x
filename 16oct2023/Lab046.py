#Problem to find the max of three numbers

a = 10
b = 20
c = 13

max = None
# can assign 0 also

if a >b and a >c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max) 