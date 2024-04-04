import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

from collections import deque

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(str, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

teachers = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teachers.append((i, j))
                
def bfs():
    q = deque()
    visited = [[False] * n for _ in range(n)]

    for t in teachers:
        for i in range(4):
            x, y = t

            while in_range(x, y):
                if arr[x][y] == "O":
                    break

                if arr[x][y] == "S":
                    return True # 감시 가능
                
                x += dxs[i]
                y += dys[i]

    return False # 감시가 불가능하다

answer = "NO"
def dfs(cur_cnt):
    global answer
    if cur_cnt == 3:
        ans = bfs()
        if not ans: # 모든 선생님이 감시가 불가능한 경우
            answer = "YES"
            return
        return
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                dfs(cur_cnt + 1)
                arr[i][j] = 'X'

dfs(0)
print(answer)
