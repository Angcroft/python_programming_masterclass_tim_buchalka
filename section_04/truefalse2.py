#   If a variable doesn't have a value or is zero then it will be False

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name != 0:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")