print("enter your your statement")
string = input()
vowels = "aeiou"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)