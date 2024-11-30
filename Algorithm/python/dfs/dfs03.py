# 부분집합 구하기
## {1}, {1,2}, {1,2,3}, {2}, {3}
N = 3

def DFS(n):
    if n == N+1:
        for i in range(1, N+1):
            if check[i] == 1:
                print(i, end = " ")
        print()
        
    else:
        check[n] = 1
        DFS(n+1)
        check[n] = 0
        DFS(n+1)

check = [0] * (N+1)
DFS(1)