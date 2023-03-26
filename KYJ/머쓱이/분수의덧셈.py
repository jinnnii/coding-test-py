def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    
    numer = denom1*numer2 + denom2*numer1
    denom = denom1*denom2
    
    g = gcd(denom, numer)
    return [numer//g, denom//g]