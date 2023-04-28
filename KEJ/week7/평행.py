def solution(dots):
    alist=[]
    for idx, (x1,y1) in enumerate(dots):
        for x2,y2 in dots[idx+1:]:
            (x3,y3),(x4,y4)= [(x,y) for x,y in dots if [x,y] not in ([x1,y1],[x2,y2])]
            a1= (y2-y1)/(x2-x1)
            a2 = (y4-y3)/(x4-x3)
            
            if a1==a2:
                return 1
    else:
        return 0