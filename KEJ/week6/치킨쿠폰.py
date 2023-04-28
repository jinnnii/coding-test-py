def solution(chicken):
    return cpChicken(chicken//10, chicken, 0)

def cpChicken(schicken, recoupon, schksum):
    if schicken>0:
        return cpChicken(recoupon//10, (recoupon//10)+(recoupon%10), schksum+recoupon//10)
    else:
        return schksum
    

def _solution(chicken):
    chksum = 0
    while chicken>=10:
        chicken, mod= divmod(chicken,10)
        chksum += chicken
        chicken+mod
    return chksum

def __solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer