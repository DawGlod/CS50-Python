import re
import sys


def convert(s):
    try:
        if matches := re.search(r"^(\d{1,2})(?::(\d{2}))? (A|P){1}M to (\d{1,2})(?::(\d{2}))? (A|P)M$", s):
            worktime = ""
            #Checking first hour
            hour_first = int(matches.group(1))
            if matches.group(2) == None:
                minutes_first = 0
            else:
                minutes_first = int(matches.group(2))
            if hour_first >= 13 or minutes_first >= 60:
                raise ValueError
            time_first = matches.group(3)
            if hour_first == 12 and time_first == "A":
                worktime += f"{hour_first-12:02d}:{minutes_first:02d} to "
            elif time_first == "A" or (hour_first == 12 and time_first == "P"):
                worktime += f"{hour_first:02d}:{minutes_first:02d} to "
            else:
                worktime += f"{hour_first+12:02d}:{minutes_first:02d} to "
            #Checking second hour
            hour_second = int(matches.group(4))
            if matches.group(5) == None:
                minutes_second = 0
            else:
                minutes_second = int(matches.group(5))
            if hour_second >= 13 or minutes_second >= 60:
                raise ValueError
            time_second = matches.group(6)
            if hour_second == 12 and time_second == "A":
                worktime += f"{hour_second:02d}:{minutes_first:02d}"
            elif time_second == "A" or (hour_second == 12 and time_second == "P"):
                worktime += f"{hour_second:02d}:{minutes_second:02d}"
            else:
                worktime += f"{hour_second+12:02d}:{minutes_second:02d}"
            return worktime
        else:
            raise ValueError
    except ValueError:
        raise


def main():
    hours = input("Hours: ")
    print(convert(hours))


if __name__ == "__main__":
    main()
