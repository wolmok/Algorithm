# https://www.acmicpc.net/problem/2667

N = int(input())  # 지도의 크기
graph = []
res = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global cnt
    # 틀린 이유
    # 처음에는 cnt = 0과 같이 함수 밖에서 선언,
    # 전역 변수를 함수 내부에서 수정하기 위해서는 반드시 ** global 키워드 사용 필요
    if x < 0 or y < 0 or x >= N or y >= N:
        return

    if graph[x][y] == 1:
        cnt += 1  # 집 개수 하나 더함
        graph[x][y] = 0  # 방문 표시 대신 0으로 바꿔줌
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)


res.sort()

print(len(res))
for item in res:
    print(item)
