#implement a function called convert that accepts a str as input

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁" )
    return str

def main():
    x = str(input())
    faces = convert(x)
    return faces

print(main())





