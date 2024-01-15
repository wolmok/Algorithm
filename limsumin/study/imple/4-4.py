# 개임 개발

import sys

sys.stdin = open("limsumin/study/imple/input.txt","rt")

N, M = map(int, input().split())
A, B, d = map(int, input().split())

# 방문 여부를 확인하는 리스트 정의
visited = [[0] * M for _ in range(N)]
visited[A][B] = 1 # 처음 시작 점은 방문 처리

map_list = []
for i in range(N):
    map_list.append(list(map(int, input().split())))

# 북동남서 순서대로 이동방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 1
turn = 0

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    # 왼쪽으로 회전 
    turn_left()
    nx = A + dx[d]
    ny = B + dy[d]
    if visited[nx][ny] == 0 and map_list[nx][ny] == 0: # 아직 가보지 않았으면서, 육지
        visited[nx][ny] = 1 # 방문 처리
        # 좌표 업데이트
        A = nx
        B = ny
        result += 1 # 이동 횟수 늘려줌
        turn = 0 # 이동을 했으므로 턴 개수는 0 으로 초기화
    else:
        turn += 1 # 턴 횟수 늘려줌
    if turn == 4: # 턴이 4방향 다 돌았을 때
        # 각 방향에서 뒤로 이동
        nx = A - dx[d]
        ny = B - dy[d]

        if map_list[nx][ny] == 0: # 육지라서 이동 가능한 경우
            A = nx
            B = ny
        else: # 바다라서 이동 불가능한 경우: 종료 조건
            break
        turn = 0 # 갔으면 턴 초기화

print(result)
        
    