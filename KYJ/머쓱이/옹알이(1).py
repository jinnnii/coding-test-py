def solution(babbling):
    answer = 0
    
    a = ['aya','ye','woo','ma']
    for b in babbling:
        tmp = ''
        for i in range(len(b)):
            tmp += b[i]
            if tmp in a:
                tmp = ''
        
        if tmp == '':
            answer += 1
                
    return answer