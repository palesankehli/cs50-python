name = str(input("camelCase: "))

snake_case = ""
for i in name:
    if i.isupper():
        snake_case += "_" + i.lower()
    else:
        snake_case += i

print("snake_case: ", snake_case)
