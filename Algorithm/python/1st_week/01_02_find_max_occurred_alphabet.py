def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    
    # 문자열 하나하나를 아스키코드로 치환한다.


    # 치환한 값을 - 97을 해줘서 0 ~ 47까지의 인덱스에 값을 더해준다.
    
    # 가장 큰 값의 인덱스에 + 97해서 출력한다.
    alphabat_occurrence_array = [0] * 26
    
    for i in string:
        if i.isalpha():
            alphabat_occurrence_array[ord(i) - ord('a')] +=1
    
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabat_occurrence_array)):
        alphabet_occurrence = alphabat_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))