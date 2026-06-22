def main():
    time = input("What time is it? ")
    result = convert(time)
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")


def convert(time):
    is_am = "a.m." in time
    is_pm = "p.m." in time
    time = time.replace(" a.m.", "")
    time = time.replace(" p.m.", "")
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    if is_am and h == 12:
        h = 0
    elif is_pm and h != 12:
        h += 12
    return h + m / 60


if __name__ == "__main__":
    main()