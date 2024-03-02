# 인구 이동
# https://www.acmicpc.net/problem/16234

# BFS 풀이

from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


day = 0

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)  # 방문 X인 나라를 bfs 처리

                if len(country) > 1:  # 인구 이동이 필요한 경우
                    flag = 1  # 플래그 변경
                    people = sum(A[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        A[x][y] = people

    if flag == 0:  # 인구 이동이 끝나면 완료
        print(day)
        break

    day += 1  # 이동이 발생할 경우 날짜 수를 1씩 증가
