def calculator(expression):
    first, sign, second = expression.split(" ")
    if sign == "+":
        return float(first) + float(second)
    elif sign == "-":
        return float(first) - float(second)
    elif sign == "*":
        return float(first) * float(second)
    elif sign == "/":
        return float(first) / float(second)


def main():
    expression = input("Expression: ").strip()
    print(calculator(expression))


if __name__ == "__main__":
    main()
