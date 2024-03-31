# 숨바꼭질

import sys
import heapq
from collections import defaultdict
sys.stdin = open("limsumin/study/부록/input.txt","rt")

INF = int(1e9)

n, m = map(int, input().split())

start = 1
graph = defaultdict(list)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, curr = heapq.heappop(q)

        if distance[curr] < dist:
            continue

        for item in graph[curr]:
            next, c = item
            cost = dist + c

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))


dijkstra(start)

num = 0
dist = -int(1e9)
count_same = 0

for i in range(1, len(distance)):
    if distance[i] == 0:
        continue
    elif dist < distance[i]:
        num = i
        dist = distance[i]
    elif dist == distance[i]:
        count_same += 1

print(num, dist, count_same)

# INF = int(1e9)

# graph = [[INF] * n for _ in range(n)]
# for _ in range(m):
#     i, j = map(int, input().split())
#     graph[i- 1][j - 1] = 1
#     graph[j- 1][i - 1] = 1

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             graph[i][j] = 0

# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# num = 0
# dist = -int(1e9)
# count_same = 0

# for j in range(n):
#     print(graph[0][j])
#     if graph[0][j] == 0:
#         continue
#     elif dist < graph[0][j]:
#         dist = graph[0][j]
#         num = j + 1
#         # count_same += 1
#     elif dist == graph[0][j]:
#         count_same += 1 

# print(num, dist, count_same)