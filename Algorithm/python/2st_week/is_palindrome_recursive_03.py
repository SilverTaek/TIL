input = "abcba"

"""
1. 배열 앞이랑 맨뒤랑 비교
2. 앞은 하나씩 증가, 뒤는 하나씩 빼기
"""
def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    
    return is_palindrome(string[1:-1])


print(is_palindrome(input))