def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
        y = d.replace("$", "")
        dollars = float(y)
        return dollars

def percent_to_float(p):

         b = p.replace("%", "")
         percentage = float(b) / 100
         return percentage
main()
