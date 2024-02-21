# 경쟁적 전염
import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")

n, k = map(int, input().split())
maps = []
virus = []


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    maps.append(list(map(int, input().split())))

    for j in range(n):
        if maps[i][j] != 0:
            virus.append((maps[i][j], i, j, 0))

s, x, y = map(int, input().split())
virus = sorted(virus)
q = deque(virus)

while q:

    cur_val, cur_x, cur_y, cur_sec = q.popleft()

    if cur_sec == s:
        break

    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 0:
            maps[nx][ny] = cur_val
            q.append((cur_val, nx, ny, cur_sec + 1))


print(maps[x-1][y-1])
