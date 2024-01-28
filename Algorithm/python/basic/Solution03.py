# K번째 큰 수
# 3장을 뽑아서 합을 기록하여 기록한 값 중 K번째로 큰 수를 출력

N, K = 10,3
A=[13,15,34,23,45,65,33,11,26,42]

answer = set()

for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            answer.add(A[i] + A[j] + A[z])

answer = list(answer)
answer.sort(reverse=True) # 내림차순
print(answer[K-1])

