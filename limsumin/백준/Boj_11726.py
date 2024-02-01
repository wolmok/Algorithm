# https://www.acmicpc.net/problem/11726
# 2xn 타일
import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())

dp = [1] * (N+1)

dp[1] = 1
for i in range(2, N+1):
    dp[i] = (dp[i -1] + dp[i-2]) 

print(dp[N] % 10007)