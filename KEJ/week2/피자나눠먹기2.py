# 최소공배수 문제
def solution(n):
    return n*6//gcd(n, 6)//6


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
