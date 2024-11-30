a = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]]

max_ans = -1

for i in range(0, len(a)):
    height_sum = 0
    weight_sum = 0
    for j in range(0, len(a)):
        height_sum += a[i][j]
        weight_sum += a[j][i]

    if height_sum > max_ans:
        max_ans = height_sum
    if weight_sum > max_ans:
        max_ans = weight_sum
sum1 = 0
sum2 = 0
for i in range(0, len(a)):
    sum1 += a[i][i]
    sum2 += a[len(a) -1 - i][i] # [4,0] [3,1] [2,2] [1, 3] [0,4]

if sum1 > max_ans:
    max_ans = sum1
if sum2 > max_ans:
    max_ans = sum2
print(max_ans)