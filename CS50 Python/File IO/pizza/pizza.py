import sys
import csv
from tabulate import tabulate

def pizza():
    try:
        if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
                file = csv.reader(file)
                return (tabulate(file, headers="firstrow", tablefmt="grid"))
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
    except FileNotFoundError:
            sys.exit("File does not exist")


def main():
    print(pizza())


if __name__ == "__main__":
    main()
