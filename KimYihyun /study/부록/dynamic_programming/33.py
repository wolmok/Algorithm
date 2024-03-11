# 퇴사
# https://www.acmicpc.net/problem/14501

N = int(input())
time_and_price = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + time_and_price[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + time_and_price[i][0]] +
                    time_and_price[i][1])
print(dp[0])
