greet = str(input("Greeting: "))
greeting = greet.lower().strip()
x = greeting.count("hello")
y = greeting.find("h")
if x != 0:
    print("$0")
elif y != 1:
    print("$20")
else:
    print("$100")
