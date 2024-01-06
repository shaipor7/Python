from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()
Input = input("Input: ")

if len(sys.argv) == 1:
    font = random.choice(font_list)
    figlet.setFont(font=font)
    print(figlet.renderText(Input))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(Input))
else:
    sys.exit("arguments are not correct")
