def solution(n):
    answer = 0
    for i in list(map(int, str(n))):
        answer += i
    return answer
