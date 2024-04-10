import sys
import csv

def scourgify():
    try:
        if len(sys.argv) == 3:
            with open(sys.argv[1], "r") as file:
                with open(sys.argv[2], "w") as file2:
                    reader = csv.DictReader(file)
                    writer = csv.writer(file2)
                    writer.writerow(["first", "last", "house"])
                    for line in reader:
                        last, first = line["name"].split(", ")
                        writer.writerow([first, last, line["house"]])
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
            sys.exit("Some file is not CSV")
    except FileNotFoundError:
        print(f"Could not find {sys.argv[1]}")
        sys.exit(1)


def main():
    scourgify()


if __name__ == "__main__":
    main()
