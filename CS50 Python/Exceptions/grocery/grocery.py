def grocery():
    items = {}
    while True:
        try:
            item = input().upper()
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            return items


def main():
    result = grocery()
    for item in sorted(result.items(), key=lambda x: x[0]):
        print(item[1], item[0])


if __name__ == "__main__":
    main()
