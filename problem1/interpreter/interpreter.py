inp = input("Expression: ")

x, op, y = inp.split(" ")

x = int(x)
y = int(y)

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y

print(f"{result:.1f}")


