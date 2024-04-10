def price(prices):
    total = 0
    while True:
        try:
            order = input("Item: ").title().strip()
            if order not in prices:
                raise ValueError
            total += prices[order]
            print(f"Total: ${total:.2f}")
        except ValueError:
            continue
        except EOFError:
            break


def main():
    prices = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    price(prices)


if __name__ == "__main__":
    main()
