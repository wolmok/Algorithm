# 상하좌우
N = int(input())  # 공간의 크기
movePlan = list(map(str, input().split())) # 이동 계획
direction = ['L', 'R', 'U', 'D']
x, y = 1, 1 # 초기 좌표

# dx, dy 테크닉 적용해서 리팩토링
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for m in movePlan:
    idx = direction.index(m)

    nx, ny = x + dx[idx], y + dy[idx]
    if nx <= 0 or ny <= 0 or nx > N or ny > N: # 무시되는 좌표 조건 설정
        continue
    else: # 아닌 경우 좌표 업데이트
        x, y = nx, ny

print(x, y)
