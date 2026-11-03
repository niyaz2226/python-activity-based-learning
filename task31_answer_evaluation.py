key = "ABCDABCD"
students = [("S1", "ABCDABCD"), ("S2", "ABC-AB-D"), ("S3", "BACDBBAD"), ("S4", "--------")]
for name, answers in students:
    correct = wrong = blank = 0
    for i in range(len(key)):
        if answers[i] == "-":
            blank += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1
    print(name, "Correct:", correct, "Incorrect:", wrong, "Unanswered:", blank, "Score:", correct * 4 - wrong)
