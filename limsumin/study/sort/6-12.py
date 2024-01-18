# 두 배열의 원소 교체

import sys

sys.stdin = open("limsumin/study/sort/input.txt","rt")

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse= True)

result = sum(A[K:]) + sum(B[:K])

print(result)