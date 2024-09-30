numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Enter the number you want it's multiplication table")
answer,second = int(input("first:")), int(input("second:"))

for numbers in range(1,13):
    result = numbers * answer
    all = numbers * second
    everything = [ result, all]
    print(str(numbers) + " x " + str(answer) + " = " + str(everything[0]) + "        " + str(numbers) + " x " + str(second) + " = " + str(everything[1])) every