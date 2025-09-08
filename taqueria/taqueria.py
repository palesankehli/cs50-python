# implement a program that enables a user to place an order, prompting them for items
# one per line, until the user inputs control-d
#After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign
#and formatted to two decimal places.
#Treat the user’s input case insensitively. Ignore any input that isn’t an item.
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:

        user_input = input("Item: ").title()
        if user_input in items:
            total += items[user_input]
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
