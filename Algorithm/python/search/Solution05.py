# 8 3
# 8개의 배열 중에서 연속된 숫자의 합이 3이 나올 수 있는 경우의 수를 구하여라

# 풀이
# 1. 2개의 포인터를 설정한다. Lt, Rt
# 2. 두 수의 합을 가지고 설정된 합과 비교하여 Lt, Rt를 정정한다.
m = 3
n = [1,2,1,3,1,1,1,2]
lt = 0
rt = 1
tot = n[0]
cnt = 0
while True:
    if tot < m:
        if rt < len(n):
            tot += n[rt]
            rt+=1
        else:
            break
    elif tot == m:
        cnt+=1
        tot -= n[lt]
        lt+=1
    else:
        tot -= n[lt]
        lt+=1


print(cnt)

