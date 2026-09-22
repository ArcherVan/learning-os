from practice3 import InvalidScoreError,validate_score
def load_scores(filename):
    scores = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    score = int(line)
                    result = validate_score(score)
                except ValueError:
                    print("数据错误。")
                    continue
                except InvalidScoreError:
                    print("成绩不合法")
                    continue
                scores.append(result)   
    except FileNotFoundError:
        print("文件不存在。")
        return []
    return scores
def main():
    scores = load_scores("not_exist.txt")
    print(scores)
if __name__ == "__main__":
    main()