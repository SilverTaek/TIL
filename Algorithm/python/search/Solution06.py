n = [[10,13,10,12,15],[12,39,30,23,11],[11,25,50,53,15],[17,27,29,37,27],[19,13,30,13,19]]

sum = []

for i in n:
    temp_x = 0
    temp_y = 0
    for j in n:
        temp_x += n[i][j]
        temp_y += n[j][i]

    sum.append(temp_x)
    sum.append(temp_y)

temp = 0

for i in n:
    temp += n[i+1][i+1]
