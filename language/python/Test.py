
# msg="It is Time"
# print(msg)
# print(msg.lower())
# print(msg.upper())

# 리스트와 튜플
# 소괄호는 리스트 대괄호는 튜플
# 트플값은 변경할 수 없지만 리스트는 변경할 수 있다.

a = [1,3,5,7,9]

# for x in enumerate(a):
#     print(x)
# print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(50>x for x in a): #모두가 참이여야 참
    print("YES")
else:
    print("NO")


if any(15>x for x in a): #한번만 참이면 전체가 참
    print("YES")
else:
    print("NO")

a=[]