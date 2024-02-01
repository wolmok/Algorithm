# 다익스트라 알고리즘 구현
import sys
from collections import defaultdict, deque


sys.stdin = open("limsumin/study/path/input.txt","rt")

INF = int(1e9)

N, M = map(int, input().split())
start = int(input())

graph = defaultdict(list)
visited = [False] * (N+1)
distance = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def get_small_idx():
    idx = 0
    for i in range(1, N+1):
        if distance[i] < INF and not visited[i]:
            idx = i
            break
    return idx


def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for item in graph[start]:
        b, c = item[0], item[1]
        distance[b] = c

    for i in range(N-1):
        cur = get_small_idx()
        visited[cur] = True

        for item in graph[cur]:
            b, c = item[0], item[1]
            distance[b] = min(distance[b], distance[cur] + c)
                
    return None
    
dijkstra(start)   

for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    

