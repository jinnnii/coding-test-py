def solution(common):
    ari = [common[i+1]- v for i,v in enumerate(common[:-1])]
    if len(set(ari))==1:
        return common[-1]+ari[0]
    else:
        return common[-1]*(common[1]/common[0])
    
    