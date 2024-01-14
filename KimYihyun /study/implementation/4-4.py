# 게임 개발
# 0 -> 육지 / 1 -> 바다
# 바다에는 접근 불가

# N -> 맵 세로 크기, M -> 맵 가로 크기
N, M = map(int, input().split())

# A -> 북쪽으로 떨어진 칸의 개수
# B -> 서쪽으로 떨어진 칸의 개수
# d -> 캐릭터가 바라보는 방향
A, B, d = map(int, input().split())

# 방문한 칸수를 저장할 변수 선언
# 초기 위치까지 세어야 하므로 1로 초기화
count = 1
# 회전한 횟수 카운트
turn_count = 0
# 방문한 위치를 저장할 맵 초기화
visited = [[0]*M for _ in range(N)]
# 처음에 위치해있던 곳은 visited 처리
d[A][B] = 1

# 반시계 방향으로 회전하는 함수


def turn_into():
    if (d != 0):
        d -= 1  # d가 동/남/서이면 -1로 반시계 회전
    elif (d == 0):
        d = 3  # d가 북이면 3 대입해 서쪽 바라보게 회전


# 방향을 나타내는 배열 선언
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # 반시계로 회전 및 좌표 계산
    turn_into()
    nx = A + dx[d]
    ny = B + dy[d]
    # if d[nx][ny] == 0 and
    if turn_count == 4:
        nx = A - dx[d]
        ny = B - dy[d]


# 방문한 칸수 출력
print(count)
