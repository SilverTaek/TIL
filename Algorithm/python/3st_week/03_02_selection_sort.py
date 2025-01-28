input = [4, 6, 2, 9, 1]

# 선택정렬
def selection_sort(array):
    # 이 부분을 채워보세요!
    input_len = len(array)

    for i in range(input_len - 1):
        min_index = i
        for j in range(input_len - i): # (4,4), (4,6), (4,2) ... 
            if array[i + j] < array[min_index]: # i=0, j=0
                min_index = i + j
        array[min_index], array[i] = array[i], array[min_index]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))