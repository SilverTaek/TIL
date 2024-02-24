# 10진수를 2진수로 재귀함수를 이용하여 만들기
# n을 2로 나눈 나머지를 기록하고 몫을 2로 나눠주는것을 반복

n = 11
ans = []

def dfs(n):
    if n == 0:
        return
    else:
        dfs(n//2)
        print(n%2, end = '')


if __name__=="__main__":
    dfs(n)

    