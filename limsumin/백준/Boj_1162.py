# https://www.acmicpc.net/problem/1162
# 도로포장

import sys
import heapq
from collections import defaultdict

sys.stdin = open("limsumin/백준/input.txt", "rt")  

INF = int(1e9)

n, m, k = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
distance = [[INF for _ in range(k+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 양방향 도로
    graph[a].append([b, c])
    graph[b].append([a, c])

def dijkstra(start):
    queue = []
    count = 0 # 도로 포장 개수
    heapq.heappush(queue, (0, start, count))
    distance[start][count] = 0

    while queue:
        cur_dist, cur_ptn, cur_cnt = heapq.heappop(queue)

        if distance[cur_ptn][cur_cnt] < cur_dist:
            continue

        for item in graph[cur_ptn]:
            b, c= item[0], item[1]

            cost = c + cur_dist

            if distance[b][cur_cnt] > cost:
                distance[b][cur_cnt] = cost
                heapq.heappush(queue, (cost, b, cur_cnt))
            if cur_cnt < k:
                if distance[b][cur_cnt + 1] > cur_dist:
                    distance[b][cur_cnt + 1] = cur_dist
                    heapq.heappush(queue, (cur_dist, b, cur_cnt + 1))

dijkstra(1)
print(min(distance[n]))
