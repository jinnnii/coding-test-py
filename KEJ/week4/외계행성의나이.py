def solution(age):
    alpha='abcdefghijklmnopqrstuvwxyz'
    return ''.join(alpha[int(i)] for i in str(age))
