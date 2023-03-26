def solution(age):
    answer = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in list(str(age)):
        answer += alphabet[int(i)]    
    return answer
