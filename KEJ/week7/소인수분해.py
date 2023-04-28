def solution(n):
    d=2
    answer=[]
    while n>1:
        if n%d==0:
            answer.append(d)
            n = n/d
        else:
            d+=1
    return sorted(list(set(answer)))