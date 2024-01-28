# 최솟값 구하기
"""
arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMIN=float('inf') # 가장 큰 값

for i in range(len(arr)):
    if arr[i] < arrMIN:
        arrMIN = arr[i]

print(arrMIN)
"""

N = 10
# N 명의 학생 중 평균을 구한 뒤, 평균에 가장 가까운 학생은 몇 번째 학생인지 출력, 만약 같은 점수대가 있다면 점수가 높은 학생의 번호가 답,
# 그리고 높은 점수를 가진 학생이 여러명이면 그중 학생번호가 빠른게 답

A = [45,73,66,87,92,67,75,79,75,80]

# 평균 구하기 = avg
# 절대값으로 A 의 원소의 차이를 기록하면서 가장 작은 값을 구함

ave = round(sum(A)/N)
min = 2147000000

for idx, x in enumerate(A):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(ave, res)


