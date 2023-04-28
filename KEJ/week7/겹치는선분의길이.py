def solution(lines):
    l1,l2,l3 = [set([i for i in range(start,end)]) for start,end in lines]
    return len(list((l1&l2)|(l2&l3)|(l1&l3)))