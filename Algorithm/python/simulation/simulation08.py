# 곳감
a = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]]

n = [[2,0,3], [5,1,2], [3,1,4]]

for i in n:
    z = i[0]
    y = i[1]
    k = i[2]

    if y == 0:
        for _ in range(k):
            a[z-1].append(a[z-1].pop(0))
    else:
        for _ in range(k):
            a[z-1].insert(0, a[z-1].pop())

print(a)