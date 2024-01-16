# 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# value 번째 사람에 대한 케빈 베이컨 수 구하기
def calculate(graph, value):
    queue = deque([])
    visited = [0 for _ in range(N+1)]
    queue.append(value)

    while queue:
        cur = queue.popleft()

        for element in graph[cur]:
            if element != value and visited[element] == 0:
                visited[element] = visited[cur] + 1
                queue.append(element)
            else:
                continue

    return sum(visited)

minimum_idx = 1
calculated = calculate(graph, 1)
for i in range(2, N+1):
    calculated_val = calculate(graph, i)

    if calculated > calculated_val:
        calculated = calculated_val
        minimum_idx = i

print(minimum_idx)

