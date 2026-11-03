ids = ["21CSE001", "22ECE045", "20MEC012", "23XYZ100", "2CSE001", "21CSE1A2"]
for s in ids:
    if len(s) != 8 or not s[:2].isdigit() or not s[2:5].isalpha() or not s[5:].isdigit():
        print(s, "-> INVALID structure")
        continue
    year = "20" + s[:2]
    branch = s[2:5]
    if branch == "CSE":
        name = "Computer Science"
    elif branch == "ECE":
        name = "Electronics"
    elif branch == "MEC":
        name = "Mechanical"
    else:
        name = "Unknown branch"
    print(s, "-> Admission year:", year, "Branch:", name, "Roll:", s[5:])
