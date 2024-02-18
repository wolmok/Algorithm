# 단지 번호 붙이기

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

N = int(input())

town = []

for _ in range(N):
    line = input()
    line_list = []

    for i in range(N):
        line_list.append(int(line[i]))
    town.append(line_list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 1

visited = [[0] * N for _ in range(N)]

def dfs(x, y, count):
    visited[x][y] = count  # 방문 처리를 여기서 해줌으로써 중복 방문을 방지
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and town[nx][ny] == 1:
            dfs(nx, ny, count)

for i in range(N):
    for j in range(N):
        if town[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j, count)
            count += 1
        
counts = []

# 단지별 크기를 세서 counts 리스트에 저장
for i in range(1, count):
    cnt = 0
    for j in range(N):
        for k in range(N):
            if visited[j][k] == i:
                cnt += 1
    counts.append(cnt)

print(len(counts))  # 단지의 개수 출력

# 각 단지의 크기를 오름차순으로 출력
for size in sorted(counts):
    print(size)