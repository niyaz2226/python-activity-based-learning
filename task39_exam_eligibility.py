students = [("Asha", 82, 10, 35, True), ("Ravi", 70, 9, 30, True), ("Meena", 78, 6, 18, True), ("Kiran", 60, 5, 15, False)]
for name, attendance, labs, internal, fee in students:
    reasons = []
    if attendance < 75:
        reasons.append("attendance below 75%")
    if labs < 8:
        reasons.append("fewer than 8 of 10 labs completed")
    if internal < 20:
        reasons.append("internal marks below 20/50")
    if not fee:
        reasons.append("fees not cleared")
    if len(reasons) == 0:
        print(name, "-> ELIGIBLE")
    else:
        print(name, "-> NOT ELIGIBLE:", ", ".join(reasons))
