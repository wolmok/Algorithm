# https://www.acmicpc.net/problem/1854
# k 번째 최단 경로

import sys
import heapq
from collections import defaultdict

sys.stdin = open("limsumin/백준/input.txt", "rt")  

INF = int(1e9)

n, m, k = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
distance = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    heapq.heappush(distance[1], 0)

    while queue:
        cur_dist, cur_ptn = heapq.heappop(queue)

        for item in graph[cur_ptn]:
            b, c = item[0], item[1]
            cost = c + cur_dist
            if len(distance[b]) <= k:
                heapq.heappush(queue, (cost, b))
                heapq.heappush(distance[b], -cost) # max-heap 으로 구현
            else:
                if distance[b][0] < -cost: # 거리 가장 긴 경로 vs 새로운 경로
                    heapq.heappop(distance[b])
                    heapq.heappush(queue, (cost, b))
                    heapq.heappush(distance[b], -cost)

                


dijkstra(1)

for i in range(1, n+1):
    if len(distance[i]) < k:
        print("-1")
    else:
        distance[i] = sorted(distance[i])
        print(-distance[i][-k])