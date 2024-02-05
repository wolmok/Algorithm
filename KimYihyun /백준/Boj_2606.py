# 바이러스
# https://www.acmicpc.net/problem/2606

from collections import deque
N = int(input())
M = int(input())

graph = []
visit = []

for _ in range(M):
    a, b = map(int, input().split())
    graph.append([a, b])

queue = deque()
queue.append(1)

while (queue):
    virus = queue.popleft()
    if virus not in visit:
        visit.append(virus)
        for i in range(M):
            if virus == graph[i][0]:
                queue.append(graph[i][1])
            elif virus == graph[i][1]:
                queue.append(graph[i][0])

print(len(visit)-1)
