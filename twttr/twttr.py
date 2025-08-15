#implement a program that prompts the user for a str of text
tweet = input("Input: ")
result = ""

for char in tweet:
    if char.lower() not in "aeiou":
        result += char
print(result)
