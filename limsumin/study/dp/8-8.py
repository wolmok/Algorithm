# 효율적인 화폐 구성

import sys

sys.stdin = open("limsumin/study/dp/input.txt","rt")

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr)

dp = [10001] * (M+1)
dp[0] = 0

for i in range(N):
    for j in range(arr[i], M+1):
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])