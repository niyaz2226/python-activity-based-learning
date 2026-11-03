roads = ["R1", "R2", "R3"]
times = ["8-9", "9-10", "10-11", "11-12"]
counts = [[300, 450, 600, 200], [150, 200, 250, 100], [500, 700, 900, 650]]
capacity = [500, 300, 800]
totals = [0, 0, 0, 0]
over = []
for i in range(len(roads)):
    for j in range(len(times)):
        c = counts[i][j]
        totals[j] += c
        ratio = c / capacity[i]
        if ratio < 0.5:
            level = "Low"
        elif ratio < 0.8:
            level = "Moderate"
        elif ratio <= 1:
            level = "High"
        else:
            level = "Over capacity"
            if roads[i] not in over:
                over.append(roads[i])
        print(roads[i], times[j], c, level)
peak = totals.index(max(totals))
print("Interval totals:", totals)
print("Peak interval:", times[peak], "with", totals[peak], "vehicles")
print("Roads exceeding capacity:", over)
