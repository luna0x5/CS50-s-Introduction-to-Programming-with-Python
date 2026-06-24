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

def main():
    while True:
        date = input("enter your date: ")
        extracted = format_extract(date)
        if extracted is None:
            continue
        month, day, year = extracted
        if not valid_m(month):
            continue
        if not valid_d(year, month, day):
            continue
        print(f"{year:04}-{month:02}-{day:02}")
        break

def format_extract(date):
    try:
        if "/" in date:
            month, day, year = date.split("/")
            return int(month), int(day), int(year)
        m_name, rest = date.split(" ", 1)
        if m_name not in months:
            return None
        day, year = rest.split(",")
        month = months.index(m_name) + 1
        return month, int(day.strip()), int(year.strip())
    except (ValueError, IndexError):
        return None


def is_leap(year):
    return (
        year % 400 == 0
        or (year % 4 == 0 and year % 100 != 0)
    )


def valid_m(month):
    return 1 <= month <= 12


def valid_d(year, month, day):
    if month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        if is_leap(year):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = 31
    return 1 <= day <= max_days


main()