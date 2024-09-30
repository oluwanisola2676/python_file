import random

print("Hello, what is your name")
name = input()

print("let me test your guessing ability")
print("guess any number number between 1 to 20")
print("so input your first guess")

y = random.randint(1,20)
z = int(input())

if z == y:
    print("correct")
else :
    print("incorrect")
    print("try again")
q = int(input())

if q == y:
    print("correct")
else :
    print("incorrect")
    print("try again")
a = int(input())
if a == y:
    print("correct")
else :
    print("incorrect")
    print("test failed")

