# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

# 3차원 행렬을 통해 벽을 부쉈는지 안부쉈는지까지 파악
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, z):
    queue = deque([])
    queue.append((x, y, z))

    while queue:
        cur_x, cur_y, cur_z = queue.popleft()

        if cur_x == N - 1 and cur_y == M - 1:
            return visited[cur_x][cur_y][cur_z]

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 and cur_z == 0: # 다음 이동할 곳이 벽이긴 하지만, 벽 부수기 기능을 안사용했을 경우
                visited[nx][ny][1] = visited[cur_x][cur_y][cur_z] + 1
                queue.append((nx, ny, 1)) # 벽 부수기 기능을 사용
            elif graph[nx][ny] == 0 and visited[nx][ny][cur_z] == 0: # 다음 이동할 곳이 벽이 아니고, 한 번도 방문하지 않은 경우
                visited[nx][ny][cur_z] = visited[cur_x][cur_y][cur_z] + 1
                queue.append((nx, ny, cur_z))
        

    return -1
    
print(bfs(0, 0, 0))