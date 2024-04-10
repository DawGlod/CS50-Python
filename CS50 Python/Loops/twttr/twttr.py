def changer(word):
    vowels = ["a", "A", "e", "E", "i" , "I", "o", "O", "u", "U"]
    new_word = []
    for sign in word:
        if sign not in vowels:
            new_word.append(sign)
    return new_word


def main():
    word = input("Input: ")
    print("Output: ", *changer(word), sep="")


if __name__ == "__main__":
    main()
