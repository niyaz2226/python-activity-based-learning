for s in ["aaabbbcccd", "abcd", "aaaaaaaaaa", ""]:
    if s == "":
        print("Empty string")
        continue
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += s[i - 1] + str(count)
            count = 1
    encoded += s[-1] + str(count)
    print(s, "->", encoded, "| Original:", len(s), "Encoded:", len(encoded), "| Beneficial" if len(encoded) < len(s) else "| Not beneficial")
