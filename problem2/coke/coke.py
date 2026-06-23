amount_due = 50
print(f"Amount due: {amount_due}")
amount_due = 50

while True:
    coin = int(input("Insert coin: "))
    if coin not in [25, 10, 5]:
        print(f"Amount due: {amount_due}")
        continue
    amount_due -= coin
    if amount_due <= 0:
        break
    print(f"Amount due: {amount_due}")

change = -amount_due       
print(f"Change owed: {change}")