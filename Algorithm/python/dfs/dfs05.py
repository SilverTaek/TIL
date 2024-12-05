# 바둑이승차
C = 259
ans = [81,58,42,33,61]
M = len(ans)

def DFS(n, sum):
    global maxguage1
    if sum > C:
        return
    if n == M:
        if maxguage1 < sum:
           maxguage1 = sum
    else:
        DFS(n+1, sum + ans[n])
        DFS(n+1, sum)

maxguage1 = -1

DFS(0, 0)
print(maxguage1)