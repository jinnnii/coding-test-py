def solution(sides):
    sides.sort()
    return 1 if sides[-1] < sum(sides[:-1]) else 2


###
def _solution(sides):
    return 1 if max(sides) > sum(sides)-max(sides) else 2
