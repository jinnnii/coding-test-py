def solution(array, height):
    answer = 0
    for i in array:
        answer += 1 if i > height else 0
    return answer
