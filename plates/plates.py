#implement a program that prompts the user for a vanity plate

#and then output Valid if meets all of the requirements
# Invalid if it does not
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):

    ...#All vanity plates must start with at least two letters.
    #vanity plates may contain a maximum of 6 characters (letters or numbers)
    if 2 >= len(str) <= 6:
   
    if not str.isalpha[0] or not str.isalpha[1]:
            return False

        for char in str:
            if  #isalpha() isnumeric()
#Numbers cannot be used in the middle of a plate; they must come at the end
#No periods, spaces, or punctuation marks are allowed
main()
