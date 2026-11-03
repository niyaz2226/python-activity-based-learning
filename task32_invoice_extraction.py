records = ["P101,2,500", "P102,x,300", "P103,5", "Q104,1,200", "P105,3,900", "P106,4,-50"]
total = 0
for r in records:
    parts = r.split(",")
    if len(parts) != 3:
        print(r, "-> MALFORMED: expected 3 fields")
        continue
    code, qty, amount = parts
    if not (len(code) > 1 and code[0] == "P" and code[1:].isdigit()):
        print(r, "-> MALFORMED: bad product code")
    elif not qty.isdigit() or not amount.isdigit():
        print(r, "-> MALFORMED: quantity and amount must be positive numbers")
    else:
        print("Code:", code, "Qty:", qty, "Amount:", amount)
        total += int(amount)
print("Total of valid amounts:", total)
