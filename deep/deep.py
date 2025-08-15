thought = str(input("What is the answer to the Great Question of Life, the Universe and Everything?"))
deep = thought.lower().strip()
if deep == "42" or deep == "forty two" or deep == "forty-two":
    print("Yes")
else:
    print("No")
