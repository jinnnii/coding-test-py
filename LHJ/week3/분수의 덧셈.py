def gcd(a,b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)        

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)    
    answer = [numer/gcd(denom, numer), denom/gcd(denom, numer)]
    return answer
