N, s, e, k = 6,2,5,3
n = [5,2,7,3,8,9]

# s부터 e까지 수를 list에 담는다.
# 오른차순 정렬한다.
# 인덱스 번호 3번째를 찾아 출력한다.

a=n[s-1:e]
a.sort()
print(a[k-1])


