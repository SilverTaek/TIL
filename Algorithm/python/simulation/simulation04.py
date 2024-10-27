# 두 리스트 합치기
a = [1, 3, 5]
b = [2, 3, 6, 7, 9]

# ans = []

# ans = a + b
# ans.sort()

# print(ans)

## a 리스트에 p1
## b 리스트에 p2
ans = []
p1 = 0
p2 = 0

while p1 < len(a) and p2 < len(b):
    if a[p1] <= b[p2]:
        ans.append(a[p1])
        p1+=1

    else:
        ans.append(b[p2])
        p2+=1

if p1 < len(a):
    ans = ans + a[p2:]
if p2 < len(b):
    ans = ans + b[p1:]

print(ans)
