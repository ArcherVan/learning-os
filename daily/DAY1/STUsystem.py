try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        scores = [int(line.strip()) for line in f if line.strip()]
except FileNotFoundError:
    scores = []
while True:
    s = int(input("输入成绩，输入-1停止录入:"))
    if s == -1:
        break
    scores.append(s)
if len(scores) == 0:
    print("暂无成绩")
else:
    students = len(scores)
    avg = sum(scores) / len(scores)
    maxscore = max(scores)
    minscore = min(scores)
    count = 0
    for score in scores:
        if score >= 60:
            count += 1
    print("学生人数为:", students)
    print("平均分:", avg)
    print(" 最高分:", maxscore)
    print(" 最低分:",  minscore)
    print(" 及格人数:", count)
with open("scores.txt", "w", encoding="utf-8") as f:
    for num in scores:
        f.write(f"{num}\n")
