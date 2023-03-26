def solution(common):
    answer = -1
    
    if (common[2] - common[1]) == (common[1]- common[0]) :
        return common[-1] + (common[1]- common[0])
    else:
        return common[-1] * (common[1] / common[0])
    
    

def solution(common):
    
    cm = common[1] / common[0]
    ca = common[1] - common[0]
    cnt1, cnt2 = 0, 0 
    p = ''
    
    for i in range(len(common)-2):
        if common[i+2] == common[i+1] * cm:
            p = 'm'
            cnt1 += 1
        
        if common[i+2] == common[i+1] + ca:
            cnt2 += 1
            p = 'a'

    if cnt1 == len(common)-2 and p == 'm':
        return common[-1]*cm
    elif cnt2 == len(common)-2 and p == 'a':
        return common[-1]+ca
    