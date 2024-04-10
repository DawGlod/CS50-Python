def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text


def main():
    text = input("Text: ")
    result = convert(text)
    print(result)


if __name__ == "__main__":
    main()
