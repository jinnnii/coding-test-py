def solution(dot):
    dic = {(True, True): 1, (False, True): 2,
           (False, False): 3, (True, False): 4}
    x, y = [x > 0 for x in dot]
    return dic[(x, y)]

###


def _solution(dot):
    ls = [(3, 2), (4, 1)]
    return ls[dot[0] > 0][dot[1] > 0]
