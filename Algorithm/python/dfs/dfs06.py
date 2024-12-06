# 중복순열
M = 3
N = 2
"""""
11
12
13
21
22
23
31
32
33
"""

#1. 1부터 M 까지 값을 담을 리스트를 생성한다.
ans = [0] * N
cnt = 0
#2. DFS 함수를 구현한다.
def DFS(level):
    global cnt
    if level == N:
        for i in range(0, N):
            print(ans[i], end = '')
        print()
        cnt = cnt + 1

    else:
        for i in range(1, M+1):
            ans[level] = i
            DFS(level+1)
DFS(0)
#3. if 문에는 N자리까지 컨트롤하기때문에 레벨 기준으로 for문을 돌려 출력해준다.
#4. 출력할 때, cnt 횟수를 올려준다.
#5. else 문에는 for문을 M까지 돌려주면서 ans배열에 하나씩 넣어주고 바로 뒤에 DFS를 레벨업해서 돌려준다.

print(cnt)
