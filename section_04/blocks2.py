name = input("Please enter your name: ")

#   The int before the input transforms the obtained string to  an integer
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote!")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("Please come back in {0} years".format(18 - age))