import inflect

p = inflect.engine()

names = []
while True:
    try:
        user_input = str(input("Name: "))
        if len(user_input) > 1:
            names.append(user_input)



    except EOFError:
        print()
        print(f"Adieu, adieu, to {p.join(names)}")
        break

