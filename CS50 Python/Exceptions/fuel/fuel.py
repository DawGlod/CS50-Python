def calculator():
    while True:
        fraction = input("Fraction: ")
        try:
            first, second = fraction.split("/")
            first = int(first)
            second = int(second)
            if first > second:
                raise ValueError
            if second == 0:
                raise ZeroDivisionError
            result = int(first) / int(second) * 100
            result = round(result, 0)
            result = int(result)
            break
        except ValueError:
            print("wrong input")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
    if result >= 99:
        return "F"
    elif result <= 1:
        return "E"
    else:
        return f"{result}%"



def main():
    print(calculator())


if __name__ == "__main__":
    main()
