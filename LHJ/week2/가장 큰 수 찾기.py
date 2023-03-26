def solution(array):
    index = 0
    answer = []
    for i in array:
        if i == max(array):
            answer = [max(array), index]
        index += 1
    return answer
