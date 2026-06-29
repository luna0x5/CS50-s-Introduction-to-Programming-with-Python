import sys
import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
        print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()