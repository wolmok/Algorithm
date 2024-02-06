# 전보
import sys
from collections import defaultdict
import heapq

sys.stdin = open("limsumin/study/path/input.txt","rt")
input = sys.stdin.readline

INF = int(1e9)

N, M, C = map(int, input().split())
graph = defaultdict(list)
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cur_dist, cur_ptn = heapq.heappop(queue)

        if distance[cur_ptn] < cur_dist:
            continue

        for item in graph[cur_ptn]:
            b, c = item[0], item[1]
            cost = cur_dist + c

            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(queue, (cost, b))

            
dijkstra(C)

count = 0
max_dist = 0

for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

print(count - 1, max_dist)

