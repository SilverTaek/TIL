n = [1, 3, 5]
m = [2, 3, 6, 7, 9]
answer = []
# 1 2 3 3 5 6 7 9
p1=p2=0
while  p1<3 and p2<5:
    if n[p1] <= m[p2]:
        answer.append(n[p1])
        p1+=1
    else:
        answer.append(m[p2])
        p2+=1
if p1<3:
    answer=answer+n[p1:]
if p2<5:
    answer=answer+m[p2:]

print(answer)


