# 연구소
# https://www.acmicpc.net/problem/14502
from collections import deque
import copy

N, M = map(int, input().split())
area = []
res = 0  # 최대 안전 영역 수

for _ in range(N):
    area.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    safe_area = copy.deepcopy(area)

    for i in range(N):
        for j in range(M):
            if safe_area[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and safe_area[nx][ny] == 0:
                safe_area[nx][ny] = 2
                queue.append((nx, ny))

    safe_count = sum(row.count(0) for row in safe_area)
    return safe_count


def makeWall(cnt):
    global res
    if cnt == 3:
        res = max(res, bfs())
        return

    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:  # 빈 칸일 때
                area[i][j] = 1  # 벽 세우기
                makeWall(cnt + 1)  # 재귀 호출 - 두 번째 벽을 세우러
                area[i][j] = 0  # 백 트래킹 (허물기)


makeWall(0)
print(res)

# makeWall 참고 코드 : https://great-park.tistory.com/104
