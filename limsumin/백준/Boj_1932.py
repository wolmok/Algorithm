# https://www.acmicpc.net/problem/1932
# 정수 삼각형

import sys

sys.stdin = open("limsumin/백준/input.txt", "rt")

n = int(input())
shape = []

for _ in range(n):
    shape.append(list(map(int, input().split())))

dp = [row[:] for row in shape]

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i - 1][j]
        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]

print(max(dp[n-1]))