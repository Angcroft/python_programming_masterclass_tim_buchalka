answer = 5;

print("Please guess number between 1 and 10: ")
guess = int(input())

#   It is not a great conditional operator, as it gets you out of loop after two wrong guesses...

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have guessed incorrectly!")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have guessed incorrectly!")
else:
    print("You got it first time")
