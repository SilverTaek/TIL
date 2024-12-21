"""""
1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
2. 각 알파벳은 중복이 가능합니다.
3. 중간에 없는 알파벳이 있을 수도 있습니다.

입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
"""

# def summarize_string(input_str):
#     # 이 부분을 채워보세요!
#     ans = ""
#     # 알파벳 아스키 코드 형태로 변환한다.
#     alphabet_occurrence_array = [0] * 26
#     for i in input_str:
#         if i.isalpha():
#             alphabet_occurrence_array[ord(i) - ord("a")]+=1
#     # 변환된 값을 배열에 ++ 시켜준다.
#     # 배열 for 문 돌면서 1이상인거 출력시켜준다. 문자열 덧셈으로

#     for index in range (0, len(alphabet_occurrence_array)):
#         if alphabet_occurrence_array[index] >=1:
           
#             ans+=chr(index+ord("a")) + str(alphabet_occurrence_array[index])

#     return ans


def summarize_string(target_string):
    # 이 부분을 채워보세요!
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))