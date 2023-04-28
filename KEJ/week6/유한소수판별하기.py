from math import gcd

def solution(a, b):
    return 2 if len(str(a/b))>15 else 1

def _solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2