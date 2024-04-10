def playback(phrase):
    for i in range(len(phrase)):
        if phrase[i] == " ":
            phrase[i] = "..."
    return phrase


def main():
    modify = list(input("Phrase: "))
    print(*playback(modify), sep="")


if __name__ == "__main__":
    main()
