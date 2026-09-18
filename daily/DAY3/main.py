from score_utils import analyze_scores
def main():
    scores = []
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
    print(analyze_scores(scores))
if __name__ == "__main__":
    main()