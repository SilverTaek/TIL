#동전교환

N = 3
ans = [1, 2, 5]
res = 9999999
sum = 15

def DFS(level, s):
    global res
    if level > res:
        return
    if s > sum:
        return
    if s == sum:
        if res > level:
            res = level
    else:
        for i in range(N):
            DFS(level+1, s+ans[i])

ans.sort(reverse = True)

DFS(0,0)
print(res)