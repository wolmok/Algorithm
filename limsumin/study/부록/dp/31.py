# 금광
# DP

import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())

    map_list = list(map(int, input().split()))
    dp = []
    for i in range(n):
        dp.append(map_list[i*m: i*m+m])

    

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][i] += max(dp[j][i - 1], dp[j + 1][i - 1])
            elif j == n-1:
                dp[j][i] += max(dp[j][i - 1], dp[j - 1][i - 1])
            else:
                dp[j][i] += max(dp[j - 1][i - 1], dp[j][i - 1], dp[j + 1][i - 1])

    res = 0
    for i in range(n):
        res = max(res, dp[i][m - 1])

    print(res)

