# 경쟁적 전염
# https://acmicpc.net/problem/18405

from collections import deque

n, m = map(int, input().split())

graph = []
data = []

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j))
data.sort()

for item in data:
    virus, virus_x, virus_y = item
    queue.append((0, virus_x, virus_y))

target_1, target_X, target_Y = map(int, input().split())

while queue:
    time, x, y = queue.popleft()
    if time == target_1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append((time + 1, nx, ny))

print(graph[target_X-1][target_Y-1])
