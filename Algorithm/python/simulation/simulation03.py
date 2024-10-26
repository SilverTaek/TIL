#카드 역배치
## a, b = b, a
str_list = [[3,5], [1,2]]

ans = [1,2,3,4,5,6,7,8,9,10]

for i in str_list:
#i[0] = 3 , i[1] = 5
    for j in range((i[1] - i[0] + 1) // 2):
        ans[i[0] -1 + j], ans[i[1] -1 - j] = ans[i[1] -1 - j], ans[i[0] -1 + j]

for x in ans:
    print(x, end= ' ') 
