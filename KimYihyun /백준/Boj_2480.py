# https://www.acmicpc.net/problem/2480

A, B, C = map(int, input().split())

if (A == B == C):
    print(10000 + A * 1000)
elif (A == B != C or A != B == C):
    print(1000 + B * 100)
elif (A == C != B):
    print(1000 + A * 100)
elif (A != B != C):
    N = max([A, B, C])
    print(N * 100)
