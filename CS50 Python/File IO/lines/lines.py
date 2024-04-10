import sys


def lines():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                counter = 0
                for line in file:
                    line = line.lstrip()
                    if line.startswith("###"):
                        counter += 1
                        continue
                    elif line.startswith("#") or len(line) == 0:
                        continue
                    else:
                        counter += 1
                return counter
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Not a python file")
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    print(lines())


if __name__ == "__main__":
    main()
