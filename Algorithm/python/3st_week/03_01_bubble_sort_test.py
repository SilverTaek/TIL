input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    # 0번 1번 교환, 1번 2번, 2번 3번 교환
    # 끝이 언제인지 어떻게알지?
    # 단 교환이 없다면 종료
    bol = False

    while():
        for i in range(0, len(array)):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                bol = True
            if i == len(array) - 1:
                if bol == False:
                    return
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))