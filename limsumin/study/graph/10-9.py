# 커리큘럼
import sys
from collections import deque
import copy

sys.stdin = open("limsumin/study/graph/input.txt","rt")

N = int(input())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]

    for j in data[1: -1]:
        indegree[i] += 1
        graph[j].append(i)


q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)


result = copy.deepcopy(time)
while q:
    cur = q.popleft()

    for i in graph[cur]:
        result[i] = max(result[i], result[cur] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)


for i in range(1, N+1):
    print(result[i])