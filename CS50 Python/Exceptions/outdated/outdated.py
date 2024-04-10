def outdated(all_months):
    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                month, day, year = date.split("/")
                day = int(day)
                month = int(month)
                year = int(year)
                if day > 31 or month > 12:
                    raise ValueError
                final_date = (f"{year}-{month:02d}-{day:02d}")
                break
            except ValueError:
                print("Invalid date")
                continue
        elif "," in date:
            try:
                month, day, year = date.split(" ")
                day = day.replace(",", "")
                day = int(day)
                year = int(year)
                if day > 31 or month not in all_months:
                    raise ValueError
                final_date = (f"{year}-{all_months.index(month)+1:02d}-{day:02d}")
                break
            except ValueError:
                print("Invalid date")
                continue
    return final_date



def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    print(outdated(months))


if __name__ == "__main__":
    main()
