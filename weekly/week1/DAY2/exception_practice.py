def safe_input_score():
    while True:
        try:
            score = int(input("请输入 0 到 100 的成绩："))
        except ValueError:
            print("请输入整数。")
            continue

        if score < 0 or score > 100:
            print("成绩范围应为 0 到 100。")
            continue

        return score
print(safe_input_score())

