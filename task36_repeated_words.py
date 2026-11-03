text = "The cat sat on the mat. The dog saw the cat, and the cat ran."
words = text.lower().replace(".", "").replace(",", "").split()
seen = []
counts = []
positions = []
for i in range(len(words)):
    w = words[i]
    if w in seen:
        k = seen.index(w)
        counts[k] += 1
        positions[k].append(i + 1)
    else:
        seen.append(w)
        counts.append(1)
        positions.append([i + 1])
for k in range(len(seen)):
    if counts[k] > 1:
        print(seen[k], "appears", counts[k], "times at positions", positions[k])
