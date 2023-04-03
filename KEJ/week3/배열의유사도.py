def solution(s1, s2):
    return len([i for i in s2 if s1.count(i) > 0])
