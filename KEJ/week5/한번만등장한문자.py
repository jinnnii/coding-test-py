def solution(s):
    return ''.join([i for i in sorted(list(set(s))) if s.count(i)==1])