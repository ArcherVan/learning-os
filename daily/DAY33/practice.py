def calculate_average(scores: list[int]) -> float:
    result = 0
    for score in scores:
        result += score
    return result/len(scores)

def count_passed(scores: list[int]) -> int:
    result = 0
    for score in scores:
        if score >= 60:
            result += 1
    return result

def get_scores(students:dict[str, int]) ->list[int]:
    scores = []
    for score in students.values():
        scores.append(score)
    return scores

def get_length(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text 必须是字符串")
    return len(text)




students = {
    "张三": 80,
    "李四": 95,
    "王五": 55
}

print(calculate_average([80, 95, 55]))
print(count_passed([80, 95, 55]))
print(get_scores(students))
print(get_length("Python"))
print(get_length(123))

