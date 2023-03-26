def solution(array):
    dic = {}
    for i in set(array):
        dic[i] = array.count(i)

    cl = list(dic.values())
    if cl.count(max(cl)) > 1:
        return -1

    for key, val in dic.items():
        if val == max(cl):
            return key
