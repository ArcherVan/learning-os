def is_pass(score):
    if score < 0 or score > 100:
        raise ValueError
    else:
        return score >= 60
