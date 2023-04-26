def solution(n):
    result = []
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            result.append(i)
            result.append(n//i)

    if i**2 ==n:
        result.remove(i)
    return sorted(result)