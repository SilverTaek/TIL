input = "abcbc"

"""
1. 배열 앞이랑 맨뒤랑 비교
2. 앞은 하나씩 증가, 뒤는 하나씩 빼기
"""
def is_palindrome(string):
    len_string = len(string)
    for i in range(0, len_string):
         if string[i] != string[len_string - i - 1]:
              return False

    return True


print(is_palindrome(input))