def count_frequency(numbers):
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    return counts
numbers = [1, 2, 2, 3, 3, 3, 4]
result = count_frequency(numbers)

def find_most_frequent(counts):
    if not counts:
        return []
    max_count = max(counts.values())
    most_frequent = []
    for number, count in counts.items():
        if count == max_count:
            most_frequent.append(number)
    return most_frequent   

print(result)
print(find_most_frequent(result))