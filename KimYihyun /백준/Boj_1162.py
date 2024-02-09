# 도로 포장
# https://www.acmicpc.net/problem/1162

import sys
import heapq

INF = sys.maxsize

N, M, K = map(int, sys.stdin.readline().rstrip().split())
road = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().rstrip().split())
    road[start].append([end, time])
    road[end].append([start, time])

dp = [[INF for _ in range(K+1)] for _ in range(N+1)]

pq = [[0, 1, 0]]

while pq:
    cur_cost, cur_road, cur_k = heapq.heappop(pq)

    if dp[cur_road][cur_k] < cur_cost:
        continue

    for next_node, next_cost in road[cur_road]:
        if dp[next_node][cur_k] > cur_cost + next_cost:
            dp[next_node][cur_k] = cur_cost + next_cost
            pq.append([cur_cost + next_cost, next_node, cur_k])

        if cur_k < K:
            if dp[next_node][cur_k+1] > cur_cost:
                dp[next_node][cur_k + 1] = cur_cost
                pq.append([cur_cost, next_node, cur_k+1])

print(min(dp[N]))
