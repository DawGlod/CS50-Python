from datetime import date
import inflect
import re
import sys


class Birthday:
    def __init__(self, birthday_date):
        self.birthday_date = birthday_date


    @property
    def birthday_date(self):
        return self._birthday_date


    @birthday_date.setter
    def birthday_date(self, birthday_date):
        if not re.match(r"^(\d{4})-(\d{2})-(\d{2})$", birthday_date):
            sys.exit("Invalid date")
        self._birthday_date = birthday_date


    def time_since_birthday_in_minutes(self):
        if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", self.birthday_date):
            year = int(matches.group(1))
            month = int(matches.group(2))
            day = int(matches.group(3))
        today = date.today()
        my_birthday = date(year, month, day)
        time_since_birthday = abs(today - my_birthday)
        return (time_since_birthday.days) * 24 * 60


    def time_since_birthday_in_minutes_in_words(self):
        p = inflect.engine()
        time_in_minutes = self.time_since_birthday_in_minutes()
        time = p.number_to_words(time_in_minutes, andword="")
        return f"{time.capitalize()} minutes"


    @classmethod
    def get(cls):
        birthday_date = input("Date of Birth: ")
        return cls(birthday_date)


def main():
    birthday = Birthday.get()
    print(birthday.time_since_birthday_in_minutes_in_words())


if __name__ == "__main__":
    main()
