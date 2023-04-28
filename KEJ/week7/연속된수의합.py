def solution(num, total):
    n=1
    nsum=-1
    while nsum!=total:
        n = n-1 if nsum>total else n+1
        nsum = sum([i for i in range(n,num+n)])
    return [i for i in range(n,num+n)]

def _solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]