def solution(money):
    x = money // 5500
    y = money - x * 5500
    answer = [x, y]
    return answer
