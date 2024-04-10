def main():
    print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    answer = input().strip().lower()
    possibilities = ["42", "forty-two", "forty two"]
    if answer in possibilities:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
