# 파티
# https://www.acmicpc.net/problem/1238

import sys
from collections import defaultdict
import heapq

sys.stdin = open("limsumin/백준/input.txt","rt")

INF = int(1e9)

n, m, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    queue = []
    distance = [INF] * (n+1)
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, cur_ptn = heapq.heappop(queue)

        if cur_dist > distance[cur_ptn]:
            continue

        for point, cost in graph[cur_ptn]:
            estimated_cost = cost + cur_dist

            if estimated_cost < distance[point]:
                distance[point] = estimated_cost
                heapq.heappush(queue, (estimated_cost, point))

    return distance


minimum = 0
for i in range(1, n+1):
    if i == x:
        continue
    else:
        distance_first = dijkstra(i)
        distance_second = dijkstra(x)
        minimum = max(distance_first[x] + distance_second[i], minimum)

print(minimum)
            
