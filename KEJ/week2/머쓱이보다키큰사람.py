def solution(array, height):
    return len([x for x in array if x > height])

###


def _solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
