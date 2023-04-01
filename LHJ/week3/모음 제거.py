def solution(my_string):
    vowel = 'aeiou'
    answer = ''
    for i in my_string:
        if i not in vowel:
            answer += i
    return answer
