def solution(A, B):
    if A==B:
        return 0
    for i in range(-1, -len(A),-1):
        if (B==A[i:]+A[:i]):
            return abs(i)
    else:
        return -1

def _solution(A,B):
    return (B+B).find(A)