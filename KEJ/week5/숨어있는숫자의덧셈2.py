import re

def solution(my_string):
    return sum([int(i) for i in re.findall('\d+',my_string)])

def _solution(my_string):
    s = [i if i.isdigit() else ' ' for i in my_string]
    return sum([int(i) for i in s.split()])