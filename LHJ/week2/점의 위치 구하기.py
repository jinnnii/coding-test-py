def solution(dot):
    if dot[0] * dot[1] > 0:
        return 1 if dot[0]>0 else 3
    else:
        return 2 if dot[0]<0 else 4
