# 1 - 7 까지 중 전위순회, 중위순회, 후위순회를 나타내시오.
## 전위순회
def dfs(n):
    if n > 7:
        return
    print(n)
    dfs(n*2)
    dfs(n*2 + 1)

dfs(1)

print('===============')
## 중위순회 
def dfs(n):
    if n > 7:
        return
    dfs(n*2)
    print(n)
    dfs(n*2 + 1)

dfs(1)
print('===============')
## 후위순회
def dfs(n):
    if n > 7:
        return
    dfs(n*2)
    dfs(n*2 + 1)
    print(n)

dfs(1)

