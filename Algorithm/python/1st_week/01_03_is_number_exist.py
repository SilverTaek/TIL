def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    is_boolean = False
    # number 랑 배열 쭉 비교해서 같은거있으면 True 아니면 False
    for i in array:
        if number == i:
            is_boolean = True

    return is_boolean


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))