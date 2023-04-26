def solution(i, j, k):
    return sum([str(i).count(str(k)) for i in range(i,j+1) if str(k) in str(i)])


def _solution(i, j, k):
    return sum([str(i).count(str(k)) for i in range(i,j+1)])