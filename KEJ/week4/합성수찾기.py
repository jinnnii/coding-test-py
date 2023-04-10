
def solution(n):
    count=0
    for i in range(1,n+1):
        if measure_count(i)>2:
            count+=1
    return count
        
def measure_count(number):
    count=1
    for i in range(2,number+1):
        if number%i==0:
            count+=1
    return count

def _solution(n):
    result=0
    for i in range(4,n+1):
        for j in range(2, int(i**.5)+1):
            if i%j==0:
                result+=1
                break