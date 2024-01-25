# 1로 만들기
import sys

sys.stdin = open("limsumin/study/dp/input.txt","rt")

X = int(input())

dp = [0] * 300001

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1 # 1을 더하는 경우
    if i % 5 == 0: # 5로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//5] + 1)
    if i % 2 == 0: # 2로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 3로 나누어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X])