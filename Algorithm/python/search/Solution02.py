n = 'g0en2Ts8eSoft'
res = 0
for i in n:
    if i.isdecimal():
        res = res*10 + int(i)
cnt = 0
print(res)

for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)



