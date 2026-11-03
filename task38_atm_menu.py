balance = 1000
log = []
actions = [(1, 5000), (2, 2000), (2, 25000), (2, 4500), (1, -10), (3, 0), (7, 0), (4, 0), (5, 0)]
print("1.Deposit  2.Withdraw  3.Balance  4.Summary  5.Exit")
i = 0
while i < len(actions):
    choice, amount = actions[i]
    i += 1
    print("\nChoice:", choice, "Amount:", amount)
    if choice == 1:
        if amount <= 0 or amount > 50000:
            print("Invalid deposit (1 to 50000)")
        else:
            balance += amount
            log.append(("Deposit", amount))
            print("Deposited. Balance:", balance)
    elif choice == 2:
        if amount <= 0:
            print("Invalid amount")
        elif amount > 10000:
            print("Limit exceeded (max 10000 per withdrawal)")
        elif balance - amount < 500:
            print("Insufficient balance (minimum 500 must remain)")
        else:
            balance -= amount
            log.append(("Withdraw", amount))
            print("Withdrawn. Balance:", balance)
    elif choice == 3:
        print("Balance:", balance)
    elif choice == 4:
        for kind, amt in log:
            print(kind, amt)
        print("Transactions:", len(log))
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice")
