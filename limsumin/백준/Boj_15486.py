# https://www.acmicpc.net/problem/15486
# 퇴사 2

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())
t_list = []
p_list = []
for _ in range(N):
    t, p = map(int, input().split())

    t_list.append(t) 
    p_list.append(p)

dp = [0] * (N+1)

for i in range(N):
    if i + t_list[i] < N+1:
        dp[i + t_list[i]] = max(dp[i + t_list[i]], dp[i] + p_list[i]) # 상담 종료일 최댓값 갱신
    dp[i+1] = max(dp[i], dp[i + 1]) # 현재 날짜 최댓값 갱신

print(max(dp))