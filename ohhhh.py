import random
numbers = random.randint(1,20)
numbers ={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"ten", 11:"Eleven",12: "Twelve", 13:"Thirteen",14:"Fourteen",
          15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"twenty"}

print("What is your name")
name = input()

print("This is a guess the number game")
print(name + " guess any number between 1 to 20")

for trials in range(1,6):
    print("enter your first number")
    answer = input()
    if answer < numbers:
        print("your guess is lower than the number")

    elif answer > numbers:
        print("your guess is higher than the number")

    else:
        break

if answer == numbers:
    print("Good job " + name + " you got the number in " +  str(trials) + " guesses")

else:
    print("you guesses are incorrect the number is " + str(numbers))