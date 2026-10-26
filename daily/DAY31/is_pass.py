def is_pass(score):
    if score < 0 or score > 100:
        raise ValueError("成绩必须在 0 到 100 之间")

    return score >= 60
