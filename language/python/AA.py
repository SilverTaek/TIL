import sys
sys.stdin=open("input.txt", "rt")

T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    print(a)
