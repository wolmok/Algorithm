# https://www.acmicpc.net/problem/3190

import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt","rt")
input = sys.stdin.readline

n = int(input())
maps = [[0] * (n+1) for _ in range(n+1)]

# 사과 관련 정보
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    maps[row][col] = 2

# 방향 변환 관련 정보
l = int(input())
dir_info = {}
for _ in range(l):
    sec, dir = map(str, input().split())
    dir_info[int(sec)] = dir

time = 0 # 시간 정보
points = deque([(1,1)]) # 뱀 위치 정보

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 x, y 값 및 초기 방향값
x, y = 1, 1
d = 0

# 뱀 시작점 세팅
maps[x][y] = 1

while True:
    nx, ny = x + dx[d], y + dy[d]

    if nx <= 0 or ny <= 0 or nx > n or ny > n or (nx, ny) in points:
        break

    # 사과 없을 경우
    if maps[nx][ny] == 0:
        row, col = points.popleft()
        maps[row][col] = 0 # 뱀이 없어짐
    x, y = nx, ny # 현재 좌표 변경
    maps[x][y] = 1
    points.append((nx, ny)) # 큐에 삽입
    time += 1 # 1초 지남

    # 방향을 바꿔야 할 타이밍
    if time in dir_info: 
        if dir_info[time] == "D": # 오른쪽 방향일 때
            d = (d+1) % 4
        else: # 왼쪽 방향
            temp_d = 3 if d == 0 else d - 1
            d = temp_d

print(time+1)