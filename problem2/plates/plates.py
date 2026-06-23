import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return False
            elif s[i:].isdigit():
                break
            else:
                return False
    return True

main()