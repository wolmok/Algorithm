# https://www.acmicpc.net/problem/1766
# 문제집

import sys
from collections import defaultdict
import heapq

sys.stdin = open("limsumin/백준/input.txt","rt")

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
res = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    res.append(cur)

    for g in graph[cur]:
        indegree[g] -= 1
        if indegree[g] == 0:
            heapq.heappush(q, g)

print(*res)