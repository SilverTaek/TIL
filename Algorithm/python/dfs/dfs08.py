# 순열
N = 3 #숫자
M = 2 #두자리

check = [0] * (N+1)

def DFS(level):
    if level == M:
        for i in range(1, N+1):
            if check[i] == 1:
                print(i, end = '')
        print()
    else:
        for i in range(1, N+1):
            check[i] = 1
            DFS(level+1)
            check[i] = 0
            DFS(level+1)

DFS(0)