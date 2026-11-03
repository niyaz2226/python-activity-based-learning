positive = ["good", "great", "excellent", "helpful"]
negative = ["bad", "poor", "boring", "slow"]
feedback = ["The teacher was great and very helpful.", "Lectures were boring and the pace was slow.", "Good content but poor labs.", "The course was okay."]
for sentence in feedback:
    words = sentence.lower().replace(".", "").replace(",", "").split()
    p = n = 0
    for w in words:
        if w in positive:
            p += 1
        elif w in negative:
            n += 1
    score = p - n
    if score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"
    print(sentence, "| Positive:", p, "Negative:", n, "Score:", score, label)
