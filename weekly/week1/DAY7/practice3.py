class InvalidScoreError(Exception):
    def __init__(self,score):
        self.score = score

def validate_score(score):
    if score >= 0 and score <= 100:
        return score
    else :
        raise InvalidScoreError(score)

