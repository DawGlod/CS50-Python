import inflect

def adieu():
    song = []
    while True:
        try:
            text = input("Name: ")
            song.append(text)
        except EOFError:
            break
    return song


def main():
    p = inflect.engine()
    result = adieu()
    print(f"Adieu, adieu, to {p.join(result)}")


if __name__ == "__main__":
    main()
