price = 50
amount_due = price

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert coin: "))

    if coin in [5, 10, 25]:
        amount_due -= coin
    else:
        print("Invalid coin")

if amount_due < 0:
    change_owed = 0 - amount_due
else:
    change_owed = 0
print("Change owed:", change_owed)

