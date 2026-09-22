def analyzer(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    cleaned = []

    for char in text:
        if char.isalnum():
            cleaned.append(char)
        else:
            cleaned.append(' ')

    text = "".join(cleaned)

    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].lower()

    counts = {}
    count = len(words)

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    if not counts:
        most_common = None
    else :
        most_common = max(counts, key=lambda word: counts[word])
    
    return counts, count, most_common
