#GUess the number
num = range(1,20)
print("Hello, what is your name")
name = input()

print("let me test your guessing ability")
print("guess any number number and if it matches means your scores increases by 10")
print("so input your first guess")

first =int(input())
if first < 5 and  first % 2 == 1:
    print("correct")
else :
    print("incorrect")


print("input your second guess")    
second = int(input())
if second > 5 and second % 3 == 2:
    print("correct")
else: 
    print("incorrect")

print("input your third guess")
import random
third = int(input())
if third % 3 == 1 and third < 5:
    print("correct")

else :
    print("incorrect")