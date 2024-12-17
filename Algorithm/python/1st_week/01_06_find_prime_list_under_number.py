input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    # 소수는 자신보다 작은 값 중에서 약수를 곱했을때 약수가 1개인것 (1, 2, 3, 5, 7, 11, 13, 17, 19)
    result = []
    for i in range(2, number + 1):
        for j in result:
            if i % j == 0:
                break
        else:
            result.append(i)

    return result


result = find_prime_list_under_number(input)
print(result)