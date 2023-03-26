def solution(num, k):
    answer = str(num).find(str(k))
    return -1 if answer == -1 else answer + 1
