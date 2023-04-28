def solution(n):
    cnt1=1
    cnt2=0
    while(cnt1):
        if cnt1%3==0 or '3' in str(cnt1):
            cnt2+=1
        if cnt1-cnt2==n:
            return cnt1
        cnt1+=1