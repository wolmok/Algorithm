# https://www.acmicpc.net/problem/16234
# 인구 이동

import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")

n, r, c= map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    temp = []
    temp.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if r <= abs(graph[nx][ny] - graph[cur_x][cur_y]) <= c:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny))

    return temp


res = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i, j)

                if len(temp) > 1: # 인구 이동 일어난 경우
                    flag = 1
                    num = sum(graph[x][y] for x, y in temp) // len(temp) # 바꿔야 하는 숫자

                    for x, y in temp:
                        graph[x][y] = num
    if flag == 0:
        print(res)
        break
    res += 1

                    
                    
