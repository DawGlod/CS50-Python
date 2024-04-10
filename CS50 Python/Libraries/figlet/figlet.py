import sys
import pyfiglet
import random

def figlet(all_fonts):
    if len(sys.argv) == 1:
        text = input("Input: ")
        result = pyfiglet.figlet_format(text, font = random.choice(all_fonts))
        return result
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in all_fonts:
        text = input("Input: ")
        result = pyfiglet.figlet_format(text, font = sys.argv[2])
        return result
    else:
        sys.exit("Invalid usage")


def main():
    all_fonts = pyfiglet.FigletFont.getFonts()
    print(f"Output: \n{figlet(all_fonts)}")


if __name__ == "__main__":
    main()
