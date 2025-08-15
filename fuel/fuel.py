def main():
    while True:
        try:
            user_input = str(input("What is X and Y? "))
            x, y = user_input.split("/")
            x = int(x)
            y = int(y)

            if x > y or y == 0:
                continue
            if x < 0 or y < 0:
                continue

            fraction = round(x / y * 100)
            if fraction <= 1:
                print("E")
            elif fraction >= 99:
                print("F")

            else:
                print(f"{fraction}%")
            break
        except (ValueError, ZeroDivisionError):
            continue





main()

