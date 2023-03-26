def solution(my_string):
    answer = []
    for i in list(my_string):
        answer.append(i.lower()) if i.isupper() else answer.append(i.upper())
    return ''.join(answer)
