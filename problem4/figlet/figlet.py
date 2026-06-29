from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Error: Invalid Usage")
        if sys.argv[2] not in fonts:
            sys.exit("Error: Invalid Usage")
        figlet.setFont(font=sys.argv[2])
    
    else:
        sys.exit("Error: Invalid Usage")
    
    inp = input("Input: ")
    print("Output:")
    print(figlet.renderText(inp), end="")

if __name__ == "__main__":
    main()