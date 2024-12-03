import sys
N = 6
ans = [1, 3, 5, 6, 7, 10]

total_sum = sum(ans)

def DFS(a, s):
    if s>total_sum//2:
        return
    if a == N:
        for i in range(0, N+1):
            print(i, end = "")
        print(" ")
        if s ==(total_sum - s): 
            print("YES")
            sys.exit(0)
    else:
        DFS(a+1, s+ans[a])
        DFS(a+1, s)

DFS(0, 0)
print("NO")