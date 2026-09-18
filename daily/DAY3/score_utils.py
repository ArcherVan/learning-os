def analyze_scores(scores):
    if not scores:
        return None
    scoresdict = dict()
    total = 0
    count = 0
    for score in scores:
        total += score
        if score >= 60:
            count += 1
    avg = total / len(scores)
    maxscore = max(scores)
    minscore = min(scores)
    pass_count = count
    scoresdict['count'] = len(scores)
    scoresdict['average'] = avg
    scoresdict['max'] = maxscore
    scoresdict['min'] = minscore
    scoresdict['pass_count'] = pass_count
    return scoresdict


    