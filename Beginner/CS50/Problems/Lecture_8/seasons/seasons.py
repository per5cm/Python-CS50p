import sys
import inflect
from datetime import date

class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.p = inflect.engine()

    def calculate_minutes(self):
        birth_date = date(self.year, self.month, self.day)
        current_date = date.today()
        delta = current_date - birth_date
        minutes = delta.days * 1440
        return self.p.number_to_words(minutes, andword="").capitalize()


def main():
    try:
        user_input = input("Date of Birth: ")
        year, month, day = user_input.split("-")
    except ValueError:
        sys.exit("Invalid Format")

    date_of_birth = Date(year, month, day)
    print(f"{date_of_birth.calculate_minutes()} minutes")


if __name__ == "__main__":
    main()
