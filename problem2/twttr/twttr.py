txt = input("Input: ")

for c in txt:
    if c.lower() in ["a", "e", "i", "o", "u", "y"]:
        txt = txt.replace(c, "")

print(txt)