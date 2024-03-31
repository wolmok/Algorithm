from collections import deque


# 현재 위치/보드를 매개변수로 받아서 이동할 다음 위치를 찾는 함수
def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    fx, fy = pos[0]
    bx, by = pos[1]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in dirs:
        nfx, nfy = fx + dx, fy + dy
        nbx, nby = bx + dx, by + dy
        if board[nfx][nfy] == board[nbx][nby] == 0:
            next_pos.append({(nfx, nfy), (nbx, nby)})

    if fx == bx:  # 로봇이 같은 행에 있으면
        for i in [1, -1]:
            if board[fx + i][fy] == board[bx + i][by] == 0:  # 좌우로 이동 O -> 따로 이동
                next_pos.append({(fx, fy), (fx + i, fy)})  # 첫 번째 이동
                next_pos.append({(bx, by), (bx + i, by)})  # 두 번째 이동
    elif fy == by:  # 로봇이 같은 열에 있으면
        for i in [1, -1]:
            if board[fx][fy + i] == board[bx][by + i] == 0:  # 상하 이동 O -> 따로 이동
                next_pos.append({(fx, fy), (fx, fy + i)})  # 첫 번째 이동
                next_pos.append({(bx, by), (bx, by + i)})  # 두 번째 이동

    return next_pos


# 보드 이동 최소 비용 구하기
def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2)
                 for _ in range(n + 2)]  # 테두리에 1 추가해서 새로운 보드 만들어서
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]  # 새 보드의 초기 상태 set

    q = deque([({(1, 1), (1, 2)}, 0)])
    visited = []

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cost + 1))
    return answer
