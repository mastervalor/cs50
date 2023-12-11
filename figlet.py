from pyfiglet import Figlet
import random
from sys import argv


figlet = Figlet()
all_fonts = figlet.getFonts()
font_count = len(all_fonts)

if len(argv) == 3  and (argv[1] == "-f" or argv[1] == "-font"):
    if argv[2] in all_fonts:
        input = str(input("Input: "))
        figlet.setFont(font=argv[2])
        print(figlet.renderText(input))
    else:
        print("Invalid usage")
        sys.exit(0)
elif len(argv) == 0:
    input = str(input("Input: "))
    rand = random.randint(0, font_count)
    figlet.setFont(font=all_fonts[rand])
    print(figlet.renderText(input))
else:
    print("Invalid usage")
    sys.exit(0)