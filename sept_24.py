# simple calculator
# calculator must be a  function
# this is a basic calculator
# ask for first and second number
# choose an operation
# operation = input(choose the operation)
# check if the user as chosen string 1,2,3,4
# else: ivalid
# again = input
# check for zero division error
#
#
#
#
def calculator():
    print("Hello there, i'm a basic calculator")
    print("I can do an operation of two numbers for you")
    print(" ")
    print("kindly enter your numbers")

    first = int(input("first number:"))
    print(" ")
    second = int(input("second number:"))

    print("Choose an operation")
    print("enter 1 for Addition, 2 for Subtraction, 3 for Multiplication and 4 for Division")
    answer = input("enter here :")

    if answer == "1":
        print(first + second)
    elif answer == "2":
        print(first - second)
    elif answer == "3":
        print(first * second)
    elif answer == "4":
        try :
            print(first / second)
        except ZeroDivisionError:
            print("Error: you tried to divide by 0")
    else:
        print("Invalid Operation")

    second_try = input("would you like to try one more time: ").lower()
    if second_try == "yes":
        calculator()
    else:
        print("Goodbye")

calculator()



    


