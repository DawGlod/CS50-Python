def decision(time):
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60



def main():
    time = input("What time is it? ")
    time = convert(time)
    print(decision(time))


if __name__ == "__main__":
    main()
