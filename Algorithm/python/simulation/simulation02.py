str = 'dkf0jkk0dkjkgjljl1kgh0ekjlkjf2lkjsklfjlkdj'

ans = 0

for i in str:
    if i.isdecimal():
        ans = ans * 10 + int(i) # 숫자 저장
print(ans)

cnt = 0
for j in range(1, ans+1):
    if ans % j == 0:
        cnt += 1

print(cnt)