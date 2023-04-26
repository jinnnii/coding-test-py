def solution(s):
    slist = s.split()
    while slist.count('Z')>0:
        zidx = slist.index('Z')
        del slist[zidx-1:zidx+1]
    return sum([int(i) for i in slist])