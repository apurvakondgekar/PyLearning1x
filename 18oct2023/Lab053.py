#Break and continue with Loops

#1 to 10 -> break if count is 5 -> 1,2,3,4,5,x

count = 1
while count <= 10:
    print(count)
    if count >= 5:
        break
    count = count + 1


# Break when count = 5
for counter in range(1,10):
    if counter == 5:
        break
    print(counter)

print("For loop has ended.")