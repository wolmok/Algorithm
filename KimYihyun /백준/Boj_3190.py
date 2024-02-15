# 뱀
# https://www.acmicpc.net/problem/3190
N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수

# 보드 초기화
board = [[0] * N for _ in range(N)]

# 사과 위치 표시
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

L = int(input())  # 뱀의 방향 변환 횟수
changes = []  # 방향 변환 정보를 저장할 리스트

# 방향 변환 정보 입력
for _ in range(L):
    sec, direction = input().split()
    changes.append((int(sec), direction))

# 초기 뱀의 위치 및 방향 설정
snake = [(0, 0)]
direction = 0  # 처음에는 오른쪽을 향하고 있음
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 시간 설정
time = 0
idx = 0  # changes 리스트를 순회하기 위한 인덱스

while True:
    time += 1

    # 다음 뱀의 머리 위치
    nx = snake[0][0] + dx[direction]
    ny = snake[0][1] + dy[direction]

    # 게임 종료 조건: 벽에 부딪히거나 자기 몸에 부딪힘
    if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) in snake:
        break

    # 뱀 머리 이동
    snake.insert(0, (nx, ny))

    # 사과를 먹지 않았을 때 꼬리 이동
    if board[nx][ny] != 1:
        snake.pop()
    else:
        board[nx][ny] = 0  # 사과 제거

    # 방향 전환
    if idx < len(changes) and time == changes[idx][0]:
        if changes[idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        idx += 1

print(time)
