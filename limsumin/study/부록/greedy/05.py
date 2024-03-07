# 볼링공 고르기

import sys
from collections import defaultdict

sys.stdin = open("limsumin/study/부록/input.txt","rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = 0

# 원래 내 풀이
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] != arr[j]:
#             res += 1

# 그리디 풀이
weights = defaultdict(int)

for i in range(len(arr)):
    weights[arr[i]] += 1

for i in range(1, m+1):
    n -= weights[i]
    res += (n * weights[i])

print(res)