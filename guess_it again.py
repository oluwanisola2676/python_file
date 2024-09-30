import random
# this is a guess the number game
print("What is your name")
name = input()

print("This is a guess the number game")
print(name + " guess any number between 1 to 20")
secret = random.randint(1,21)

for trials in range(1,6):
    print("enter your guessed number")
    answer = int(input())
    if answer < secret:
        print("your guess is lower than the number")

    elif answer > secret:
        print("your guess is higher than the number")

    else:
        break

if answer == secret:
    print("Good job " + name + " you got the number in " +  str(trials) + " guesses")

else:
    print("you guesses are incorrect the number is " + str(secret))