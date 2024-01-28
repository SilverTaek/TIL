# 자릿수의 합
"""
각 자연수의 자릿수의 합을 구하라
그리고 그 합이 최대인 자연수를 출력하라

"""

# for i in range(len(str)):
#     sum = 0
#     x = str[i]
#     while x>0:
#         sum+=x%10
#         x=x//10
#     if sum > max:
#         max = sum
#         res = str[i]

# print(res)


str1 = [125, 15232, 97]

def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum
max = -2147000000

for x in str1:
    tot=digit_sum(x)
    print(x)
    if tot>max:
        max=tot
        res=x
print(res)

