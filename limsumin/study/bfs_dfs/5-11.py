# 미로 탈출
import sys
from collections import deque

sys.stdin = open("limsumin/study/bfs_dfs/input.txt","rt")

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

queue = deque([])

queue.append((0, 0)) # queue 에 초기값 넣어주기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    cur_x, cur_y = queue.popleft() # 현재 요소 빼주기
    for i in range(4): # 동서남북 한칸씩
        nx, ny = cur_x + dx[i], cur_y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M: # 이동 조건이 성립이 안되는 경우
            continue
        if graph[nx][ny] == 0: # 귀신이 있어서 이동할 수 없는 경우
            continue
        if graph[nx][ny] == 1: # 아직 이동 안해본 이동 가능한 칸
            queue.append((nx, ny))
            graph[nx][ny] = graph[cur_x][cur_y] + 1 # 누적 업데이트
        
print(graph[N-1][M-1])     