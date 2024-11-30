
# 사과나무
a = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]]

s = e = len(a) // 2
ans = 0
for i in range(0, len(a)):
    for j in range(s, e+1):
        ans += a[i][j]

    if i < len(a) // 2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
    
print(ans)