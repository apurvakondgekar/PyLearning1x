# Match the name

name = input("Enter your name")

match name:
    case "raj":
        print("Your name was registered.")
    case "neha":
        print("Your name was registered.")
    case _:
        print("Sorry. Your name was not found.")