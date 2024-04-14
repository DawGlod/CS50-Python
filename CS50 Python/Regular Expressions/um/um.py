import re
import sys

def count(s):
    matches = re.findall(r"(\b|\s){1}um(\.|,|\?|\b|\s){1}", s, re.IGNORECASE)
    return (len(matches))


def main():
    text = input("Text: ")
    print(count(text))


if __name__ == "__main__":
    main()
