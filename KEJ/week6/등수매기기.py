def solution(score):
    avgscore = sorted([sum(i)/2 for i in score], reverse =True)
    return [avgscore.index(sum(i)/2) +1 for i in score]