
def main():
    word = input("Input: ")
    word = shorten(word)
    print(word)


def shorten(word):
    for c in word:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(c, "")
    return word


if __name__ == "__name__":
    main()
