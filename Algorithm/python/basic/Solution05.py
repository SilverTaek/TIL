# 정다면체
N, M = 4,6

answer = [0] * (N+M+3)
max = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        answer[i+j]+=1
for i in range(N+M+1):
    if answer[i] > max:
        max=answer[i]
for i in range(N+M+1):
    if answer[i] == max:
        print(i, end=' ')


