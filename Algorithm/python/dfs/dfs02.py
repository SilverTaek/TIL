n = 11
# 1011

ans = 0 

def dfs(number):
    if number == 0:
        return
    
    dfs(number // 2)
    print(number % 2, end ='')


dfs(n)