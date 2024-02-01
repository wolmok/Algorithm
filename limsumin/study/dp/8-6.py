# 개미전사
import sys

sys.stdin = open("limsumin/study/dp/input.txt","rt")

N = int(input())
store_list = list(map(int, input().split()))

dp = [0] * 100
dp[0] = store_list[0]
dp[1] = max(store_list[0], store_list[1])

for i in range(2, N):
    # 바로 앞 원소를 선택한 경우와 그렇지 않고 이번 원소를 같이 선택한 경우
    dp[i] = max(dp[i-1], dp[i-2] + store_list[i])

print(max(dp))