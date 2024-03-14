# 정확한 순위
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# print('N', N, 'M', M, 'A', A, 'B', B)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1


for p in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][p], graph[p][b])

for i in range(1, N+1):
    global res
    res = 0
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1

    if cnt == N:
        res += 1

print(res)
