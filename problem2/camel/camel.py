s = input("camelCase: ")
snake = ""
for c in s:
    if c.isupper():
        snake += "_"
        snake += c.lower()
        continue
    snake += c

print("snake_case:", snake)