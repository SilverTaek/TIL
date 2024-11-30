# 수들의 합
## 연속된 숫자 합이 n 이 되는 cnt를 구하시오

n = 3
a = [1,2,1,3,1,1,1,2]

ans = 0

lt = 0
rt = 1

tot = a[0]

while True:
    if tot < n:
        if rt < len(a):
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot == n:
        ans+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(ans)