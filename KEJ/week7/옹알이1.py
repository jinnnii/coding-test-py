def solution(babbling):
    answer=0
    for i in babbling:
        s = i
        for babb in ['aya','ye','woo','ma']:
            s = s.replace(babb,' ')
        s = s.replace(' ','')
        if s=='':
            answer+=1
    return answer