import random

def main():


    wins = 0
    level = get_level()

    for _ in range(10):
        tries = 0
        
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        while tries < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if answer != user_input:
                    tries += 1
                    print("EEE")
                else:
                    wins += 1
                    break
            except ValueError:
                tries += 1

        if tries >= 3:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {wins}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
           pass


def generate_integer(n):

   if n == 1:
        return random.randint(0, 9)
   elif n == 2:
        return random.randint(10, 99)
   else:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()
