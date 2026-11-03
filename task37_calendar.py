for start, days in [(2, 30), (0, 31), (5, 28), (4, 32)]:
    if start < 0 or start > 6 or days < 28 or days > 31:
        print("Invalid input:", start, days)
        continue
    print("Mo Tu We Th Fr Sa Su")
    line = "   " * start
    for d in range(1, days + 1):
        line += str(d).rjust(2) + " "
        if (d + start) % 7 == 0:
            print(line)
            line = ""
    if line != "":
        print(line)
    print()
