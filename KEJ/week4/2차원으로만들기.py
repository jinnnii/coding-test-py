def solution(num_list, n):
    result=[]
    while num_list:
        _result=[]
        for _ in range(n):
            _result.append(num_list.pop(0))
        result.append(_result)
    return result


def _solution(num_list, n):
    result=[]
    for i in range(0, len(num_list),n):
        result.append(num_list[i:i+n])
    return result