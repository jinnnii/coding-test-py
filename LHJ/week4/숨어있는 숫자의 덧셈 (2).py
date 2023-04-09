def solution(my_string):
    number = '';
    for i in my_string:
        if i.isalpha():
            number += ' '
        else:
            number += i
            
    return sum(list(map(int, number.split())))
