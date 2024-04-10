def main():
    greeting = input("Greeting: ").strip()
    if greeting.startswith("Hello"):
        x = 0
    elif greeting.startswith("H"):
        x = 20
    else:
        x = 100
    print(f"${x}")


if __name__ == "__main__":
    main()
