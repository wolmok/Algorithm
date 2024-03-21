# 상자넣기
# https://www.acmicpc.net/problem/1965

N = int(input())
box = list(map(int, input().split()))
graph = [1] * N


def insert_box(box):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if box[j] < box[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)


print(insert_box(box))
