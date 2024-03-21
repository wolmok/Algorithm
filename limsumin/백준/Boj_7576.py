# https://www.acmicpc.net/problem/7576
# 토마토

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

m, n = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
q = deque()

def bfs():
    global q
    while q:
        cur_x, cur_y, cur_cost = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cur_x + dx, cur_y + dy

            if in_range(nx, ny) and arr[nx][ny] == 0:
                arr[nx][ny] += (cur_cost + 1)
                q.append((nx, ny, cur_cost + 1))

def simulate():
    zero_count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j, 0))
            if arr[i][j] == 0:
                zero_count += 1
    
    return zero_count


def is_all_set():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                return False
            
    return True

days = 0
zero_count = simulate()
# print(q)
if zero_count == 0:
    print(0)
    exit(0)
bfs()

# print(arr)

for item in arr:
    for i in item:
        if i == 0:
            print(-1)
            exit(0)
    days = max(days, max(item))

print(days)  