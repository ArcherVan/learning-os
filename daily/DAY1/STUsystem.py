from pathlib import Path
SCORES_FILE = Path(__file__).with_name("scores.txt")

def load_scores(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_scores(filename, scores):
    with open(filename, "w", encoding="utf-8") as f:
        for score in scores:
            f.write(f"{score}\n")
    
def input_scores(scores):
    while True:
        raw = input("输入成绩，输入 -1 停止录入：")
        if raw == "-1":
            break
        try:
           s = int(raw)
        except ValueError:
            print("请输入整数。")
            continue
        if s < 0 or s > 100:
            print("成绩范围应为 0 到 100。")
            continue
        scores.append(s)
    return scores

def calculate_average(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def get_max_score(scores):
    if not scores:
        return None
    return max(scores)

def get_min_score(scores):
    if not scores:
        return None
    return min(scores)

def count_pass(scores):
    if not scores:
        return None
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    return count

def main():
    scores = load_scores(SCORES_FILE)
    scores = input_scores(scores)

    if not scores:
        print("暂无成绩")
    else:
        print("学生人数为:", len(scores))
        print("平均分:", calculate_average(scores))
        print("最高分:", get_max_score(scores))
        print("最低分:", get_min_score(scores))
        print("及格人数:", count_pass(scores))

    save_scores(SCORES_FILE, scores)
if __name__ == "__main__":
    main()