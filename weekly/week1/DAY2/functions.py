def calculate_average(scores) :
    if not scores:
        return None
    return sum(scores) / len(scores)
def count_pass(scores) :
    if not scores:
        return None
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count
def get_max_score(scores) :
    if not scores:
        return None
    return max(scores)
def get_min_score(scores) :
    if not scores:
        return None
    return min(scores)
def main():
    test_cases = [
        [100, 90, 80, 70],
        [100],
        [],
    ]

    for scores in test_cases:
        print("成绩：", scores)
        print("平均分：", calculate_average(scores))
        print("最高分：", get_max_score(scores))
        print("最低分：", get_min_score(scores))
        print("及格人数：", count_pass(scores))

if __name__ == "__main__":
    main()
