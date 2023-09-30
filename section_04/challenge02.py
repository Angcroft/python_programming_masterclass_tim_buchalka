#   Write a small program to ask for a name and an age.
#   When both values have been entered, check if the person is the right age to go on an 18-30
#   holiday (they must be over 18 and under 31).
#   If they are, welcome them to the holiday, otherwise print a polite message refusing them entry.

print("Please enter your name: ")
name = input()

print("And now enter your age: ")
age = int(input())

if 18 <= age and age < 31:
    print("Welcome {}! You're allowed to enter!".format(name))
else:
    if age < 18:
        print("You're too young to enter, I'm sorry")
    elif age >= 31:
        print("You're too old to enter, I'm sorry")