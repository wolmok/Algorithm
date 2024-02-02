# https://www.acmicpc.net/problem/2606
# 바이러스

import sys
from collections import defaultdict, deque

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())
M = int(input())

graph = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


queue = deque([])
queue.append(1)
visited[1] = True

while queue:
    cur = queue.popleft()

    for item in graph[cur]:
        if not visited[item]:
            visited[item] = True
            queue.append(item)


print(sum(visited) - 1)