def machine():
    i = 50
    acceptable = [25, 10, 5]
    while i > 0:
        coin = int(input("Instert Coin: "))
        if coin in acceptable:
            print(f"Amount Due: {i - coin}")
            i -= coin
        else:
            print(f"Amount Due: {i}")
        if i <= 0:
            print(f"Change Owed: {-i}")


def main():
    machine()


if __name__ == "__main__":
    main()
