def solution(dots):
    xx, yy = 0,0
    for idx, (x,y) in enumerate(dots[:-1]):
        xx = max(abs(x-dots[idx+1][0]), xx)
        yy = max(abs(y-dots[idx+1][1]), yy)
    return xx*yy

def _solution(dots):
    return (max(dots)[0] - min(dots)[0])* (max(dots)[1]-min(dots)[1])
