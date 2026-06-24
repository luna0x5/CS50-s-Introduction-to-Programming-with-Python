def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if y == 0 or x > y:
                continue
        except ValueError:
            continue
        else:
            fuel = round((x / y) * 100)
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel}%")
            break


main()