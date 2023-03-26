def solution(n):
    answer = 0

    if n%7:
        answer = n//7 + 1
    else:
        answer = n//7
    return answer


def solution(n):
    return (n - 1) // 7 + 1