def solution(quiz):
    answer=[]
    for q in quiz:
        exp, val = q.split('=')
        exp = sum([int(i) for i in exp.replace(' - ',' +- ').replace(' ','').replace('--','').split('+')])
        ox = 'O' if exp==int(val) else 'X'
        answer.append(ox)
    return answer
        