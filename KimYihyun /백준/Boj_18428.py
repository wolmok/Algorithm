# 감시 피하기
# https://www.acmicpc.net/problem/18428

N = int(input())
graph = []
teacher = []
hide = False


def backtracking(cnt):
    global hide

    if cnt == 3:
        if bfs():
            hide = True
            return
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    backtracking(cnt + 1)
                    graph[i][j] = "X"


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:
        for k in range(4):
            nx, ny = t
            while 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == "O":
                    break
                if graph[nx][ny] == "S":
                    return False

                nx += dx[k]
                ny += dy[k]

    return True


for i in range(N):
    M = list(map(str, input().split()))
    graph.append(M)
    for j in range(N):
        if graph[i][j] == "T":
            teacher.append((i, j))

backtracking(0)

if hide:
    print("YES")
else:
    print("NO")
