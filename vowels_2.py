print("enter your statement")
string = input()
vowels = "aeiou"

count = sum(string.count(vowels) for vowels in vowels)

print(count)