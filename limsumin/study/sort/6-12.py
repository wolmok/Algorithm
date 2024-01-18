# 두 배열의 원소 교체

import sys

sys.stdin = open("limsumin/study/sort/input.txt","rt")

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse= True)

# 이렇게 하면 A 에 있는 원소들이 B 보다 클 수도 있는 경우를 고려 못함
# result = sum(A[K:]) + sum(B[:K])

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]

print(sum(A))