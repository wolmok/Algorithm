# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

N = int(input())


def cal(N):
    if N <= 3:
        dp = [1, 2, 4]
        return dp[N-1]
    else:
        dp = [1, 2, 4] + [0] * (N - 3)
        for i in range(3, N):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[-1]


for i in range(N):
    print(cal(int(input())))
