"""
level
moon
abcba
soon
gooG
"""

list = ["level", "moon", "abcba", "soon", "gooG"]

def lotation(str):
    flag = False
    
    for k in range(0, len(str)//2):
        if str[k] != str[-1-k]:
            flag = True
    return flag

for i in range(0, len(list)):
    temp = list[i].lower()
    if lotation(temp):
        print("NO")
    else:
        print("YES")

