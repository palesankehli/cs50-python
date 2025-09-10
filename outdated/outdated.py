# implement a program that prompts the user for a date, in month-day-year order
#Then output that same date in YYYY-MM-DD format
#If the user’s input is not a valid date in either format, prompt the user again
#Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days


months = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    try:
        date = str(input("Date: ")).title()
        if "/" in date:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
        else:
            month, day, year = date.split()
            month = months.index(month) + 1
            if "," in day:
                day = day.strip(",")
            else:
                raise ValueError
            day, year = int(day), int(year)

        if 1 <= month >= 12 or 1 <= day >= 31:
            raise ValueError
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        continue





