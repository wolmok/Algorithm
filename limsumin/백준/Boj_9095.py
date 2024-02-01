# https://www.acmicpc.net/problem/9095
# 1,2,3 더하기

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

def cal_count(number):
    answer = 0
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, number+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[number] 

T = int(input())

for _ in range(T):
    number = int(input())
    print(cal_count(number))