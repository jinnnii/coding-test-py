def solution(rsp):  
    answer = []
    for i in list(str(rsp)):
        if i == '0':
            answer.append('5')
        elif i == '2':
            answer.append('0')
        elif i == '5':
            answer.append('2')
    return ''.join(answer)
