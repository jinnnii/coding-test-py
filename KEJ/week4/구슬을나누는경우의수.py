
import math
def fac(num):
    result=1
    for i in range(1,num+1):
        result *= i
    return result

def solution(balls, share):
    return fac(balls)/(fac(balls-share)*fac(share))