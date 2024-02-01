# 미래 도시
import sys

sys.stdin = open("limsumin/study/path/input.txt","rt")

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 이동 고려
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for i in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = graph[1][K] + graph[K][X]

if result >= INF:
    print("-1")
else:
    print(result)