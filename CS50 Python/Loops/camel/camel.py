def cameltosnake(camel):
    new_word = []
    for sign in camel:
        if sign.isupper():
            sign = (f"_{sign.lower()}")
            new_word.append(sign)
        else:
            new_word.append(sign)
    return new_word



def main():
    camel = input("camelCase: ")
    print(*cameltosnake(camel), sep="")

if __name__ == "__main__":
    main()
