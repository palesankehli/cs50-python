from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts = figlet.getFonts()
#Expects zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
  font = random.choice(fonts)

#Two if the user would like to output text in a specific font,
# in which case the first of the two should be -f or --font,
# and the second of the two should be the name of the font.

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
  font = sys.argv[2]
else:
  sys.exit("Invalid usage")

figlet.setFont(font=font)




  # and the second of the two should be the name of the font.

user_input = str(input("Input: "))
print(figlet.renderText(user_input))
#Outputs that text in the desired font.
