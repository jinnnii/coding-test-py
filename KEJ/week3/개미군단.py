def solution(hp):
    result1, num = divmod(hp, 5)
    result2, num = divmod(num, 3)
    result3, num = divmod(num, 1)
    return sum([result1, result2, result3])
