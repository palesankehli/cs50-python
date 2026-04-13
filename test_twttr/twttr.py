def main():
    string_input = str(input("Input: "))
    result = shorten(string_input)
    print(result)

def shorten(string_input):
    new_word = ""
    for char in string_input:
        if char not in "aeiou":
            new_word += char
    return new_word

if __name__ == "__main__":
    main()
