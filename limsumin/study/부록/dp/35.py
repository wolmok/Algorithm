# 못생긴 수

import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

# 내 풀이
# n = int(input())

# dp = [0] * 1001

# dp[1] = 1

# cnt = 1

# for i in range(2, 1001):
#     if cnt == n:
#         break

#     if i % 2 == 0 and dp[i // 2]:
#         dp[i] = i
#         cnt += 1
#     elif i % 3 == 0 and dp[i // 3]:
#         dp[i] = i
#         cnt += 1
#     elif i % 5 == 0 and dp[i // 5]:
#         dp[i] = i
#         cnt += 1

# print(max(dp))

# 책 풀이
n = int(input())
dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0
n2, n3, n5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(n2, n3, n5)

    if dp[i] == n2:
        i2 += 1
        n2 = dp[i2] * 2
    if dp[i] == n3:
        i3 += 1
        n3 = dp[i3] * 3
    if dp[i] == n5:
        i5 += 1
        n5 = dp[i5] * 5

print(dp[n - 1])