
def solution(array):
    answer = -1
    dic = dict()

    for a in array:
        if a not in dic:
            dic[a] = array.count(a)    

    dic = sorted(dic.items(), key = lambda item : item[1] , reverse=True)
    print(dic)
    if len(dic) > 1 and dic[0][1] != dic[1][1] or len(dic) == 1:
        answer = dic[0][0]

    return answer


def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1