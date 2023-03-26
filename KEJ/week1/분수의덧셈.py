def solution(numer1, denom1, numer2, denom2):
    _denom = denom1*denom2
    _numer = (numer1*denom2)+(numer2*denom1)
    _gcd = gcd(_denom, _numer)
    return [_numer/_gcd, _denom/_gcd]


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
