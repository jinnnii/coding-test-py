def solution(num_list):
    result = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            result[0] = result[0]+1
        else:
            result[1] = result[1]+1
    return result

def _solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer