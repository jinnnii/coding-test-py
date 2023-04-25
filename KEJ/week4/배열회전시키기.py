
def solution(numbers, direction):
    direct = -1 if direction=="right" else 1
    return  numbers[direct:]+numbers[:direct]