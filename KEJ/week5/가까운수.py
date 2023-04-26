def solution(array, n):
    array.sort()
    result = [array[0], abs(array[0]-n)]
    for i in array[1:]:
        if result[1] > abs(i-n):
            result = [i, abs(i-n)]
    return result[0]


def _solution(array, n):
    array.sort(key=lambda x:(abs(x-n),x-n))
    return array[0]