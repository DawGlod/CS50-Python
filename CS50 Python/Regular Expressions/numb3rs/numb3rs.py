import re
import sys


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip.strip()):
        numbers = []
        for i in range(4):
            numbers.append(matches.group(i+1))
        numbers = list(map(int, numbers))
        for number in numbers:
            if not 0 <= number <= 255:
                return False
        return True
    else:
        return False


def main():
    print(validate(sys.argv[1]))


if __name__ == "__main__":
    main()
