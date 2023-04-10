
def solution(n):
    fac = 1
    for i,v in enumerate(range(1,11)):
        fac*=v
        if fac>n:
            return i
        elif fac==n:
            return i+1
