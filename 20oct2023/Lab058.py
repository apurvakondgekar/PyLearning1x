#Match
#Similar to switch in Java

number = int(input("Enter a number"))

match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case _: #If nothing is matching this will run
        print("No Idea")