# 우선순위큐를 이용하여 다익스트라 알고리즘 구현
# 우선순위큐는 heap 구조로 구현 될 수 있음

import sys
from collections import defaultdict
import heapq

sys.stdin = open("limsumin/study/path/input.txt","rt")

INF = int(1e9)

N, M = map(int, input().split())
start = int(input())

graph = defaultdict(list)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 거리 - 지점 순
    distance[start] = 0

    while queue:
        cur_dist, cur_ptn = heapq.heappop(queue)

        if cur_dist > distance[cur_ptn]: # 현재 노드가 이미 처리 된 적 있는지 확인
            continue

        for item in graph[cur_ptn]:
            b, c = item[0], item[1]

            cost = cur_dist + c
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(queue, (cost, b))

    return None

dijkstra(start)


for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    


