def solution(num, k):
    result = str(num).find(str(k))
    return -1 if result==-1 else result+1