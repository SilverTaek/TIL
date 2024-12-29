def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

"""
5 * re(4) // 120
4 * re(3) // 24
3 * re(2) // 6
2 * re(1) // 1
1

"""