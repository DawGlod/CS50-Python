def convert(fraction):
    while True:
        try:
            first, second = fraction.split("/")
            first = int(first)
            second = int(second)
            if first > second:
                fraction = input("Fraction: ")
                continue
            result = int(first) / int(second) * 100
            result = int(round(result, 0))
            return result
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


if __name__ == "__main__":
    main()
