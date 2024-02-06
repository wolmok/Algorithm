# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
# input time-out

import sys
import heapq
from collections import defaultdict

# sys.stdin = open("limsumin/백준/input.txt", "rt")  # Commenting this line out

INF = int(1e9)

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = defaultdict(list)
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cur_w, cur_p = heapq.heappop(q)

        if cur_w > distance[cur_p]:
            continue

        for b, c in graph[cur_p]:
            cost = cur_w + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))


dijkstra(start)

print(distance[end])
