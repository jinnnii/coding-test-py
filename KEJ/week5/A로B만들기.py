def solution(before, after):
    result = list(before)
    for i in after:
        if i in result:
            result.remove(i)
    return 1 if len(result)==0 else 0