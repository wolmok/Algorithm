# https://www.acmicpc.net/problem/14502 
# 연구소
# PyPy3 으로 채점

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

input = sys.stdin.readline
n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 0
temp = [[0] * m for _ in range(n)]

def virus(x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

def calSafeZone():
    c = 0 
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                c += 1
    return c

def dfs(count):
    global ans 
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = maps[i][j]
        

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        ans = max(ans, calSafeZone())

        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                count += 1
                dfs(count)
                maps[i][j] = 0
                count -= 1

dfs(0)
print(ans)