# 자릿수의 합
"""
각 자연수의 자릿수의 합을 구하라
그리고 그 합이 최대인 자연수를 출력하라

"""
str = [125, 15232, 97]
max = -2123233

for i in range(len(str)):
    sum = 0
    x = str[i]
    while x>0:
        sum+=x%10
        x=x//10
    if sum > max:
        max = sum
        res = str[i]

print(res)

