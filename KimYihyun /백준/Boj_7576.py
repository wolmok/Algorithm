# 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque

M, N = map(int, input().split())  # 가로 / 세로
storage = [list(map(int, input().split())) for _ in range(N)]
tomato = deque([])
day = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# row로 단순 append해줬지만, 1일 경우에 tomato에 append하는 로직을 고려하지 못해서 틀림
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            tomato.append([i, j])

# 1: 익음 / 0: 익지 않음 / -1: 토마토 없음


def bfs():
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and storage[nx][ny] == 0:
                storage[nx][ny] = storage[x][y] + 1
                tomato.append([nx, ny])


bfs()

for i in storage:
    for j in i:  # 여기서 인덱스 실수
        if j == 0:
            print(-1)
            exit(0)

    day = max(day, max(i))

print(day - 1)  # 여기서 -1 안해줌 ㅠㅠ
