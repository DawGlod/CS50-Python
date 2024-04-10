def shorten(word):
    vowels = ["a", "A", "e", "E", "i" , "I", "o", "O", "u", "U"]
    new_word = ""
    for sign in word:
        if sign not in vowels:
            new_word += sign
    return new_word


def main():
    word = input("Input: ")
    print("Output: ", shorten(word), sep="")


if __name__ == "__main__":
    main()
