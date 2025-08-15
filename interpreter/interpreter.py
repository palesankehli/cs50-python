def interpreter():
    expression = str(input("Enter expression: "))
    x, y, z = expression.split(" ")

    a = float(x)
    b = float(z)

    if y == "+":
        return a + b
    if y == "-":
        return a - b
    if y == "*":
        return a * b
    if y == "/":
        return a / b

print(interpreter())
