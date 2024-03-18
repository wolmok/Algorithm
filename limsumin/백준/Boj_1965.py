# 상자넣기
# https://www.acmicpc.net/problem/1965
# 가장 긴 증가하는 부분수열

import sys

sys.stdin = open("limsumin/백준/input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


print(max(dp))

