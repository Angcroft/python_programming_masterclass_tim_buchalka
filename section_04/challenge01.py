#   Change the condition on line 6 to 'if guess == answer'
#   then change the program to give the correct results

answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it the first time!")
else:
    if guess < answer:
        print("Please guess higher")
        guess = int(input())
        if guess != answer:
            print("Sorry, you have not guessed correctly!")
    else:
        print("Please guess lower")
        guess = int(input())
        if guess != answer:
            print("Sorry, you have not guessed correctly!")