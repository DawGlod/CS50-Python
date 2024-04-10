def value(greeting):
    greeting = greeting.strip().capitalize()
    if greeting.startswith("Hello"):
        x = 0
    elif greeting.startswith("H"):
        x = 20
    else:
        x = 100
    return x


def main():
    greeting = input("Greeting: ")
    x = value(greeting)
    print(f"${x}")


if __name__ == "__main__":
    main()
