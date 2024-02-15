# 뱀

N = int(input())  # 보드의 개수
K = int(input())  # 사과의 개수
board = [[0]*N for _ in range(N)]  # 2차원 리스트
time = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    # 행 열
    x, y = int(input().split())
    board[x][y] = 1

L = int(input())  # 뱀의 방향 변환 횟수
change = []  # 방향 변환 정보

for _ in range(L):
    sec, direction = map(str, input().split())  # sec초 뒤에 direction도 만큼 회전
    change.append(int(sec), direction)

snake = []

dir = 1  # 처음에 오른쪽
nx, ny = 0, 0  # 처음에 (0,0)에서 시작

while True:
    time += 1
    nx += dx[dir]
    ny += dy[dir]

    # 벽 or 몸에 닿으면 게임 끝
    if (nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 1):
        break

print(time)
