# https://www.acmicpc.net/problem/11722
# 가장 긴 감소하는 수열

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())
arr = list(map(int, input().split()))

# dp 초기화
dp = [1 for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))