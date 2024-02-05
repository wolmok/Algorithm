# 미래 도시
n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 갈 때 0
for i in range(n+1):
    graph[i][i] = 0

# 연결된 경우에는 1 + 양방향 고려
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 바로 가는 graph[a][b]
            # k번 노드 거쳐가는 graph[a][k] + graph[k][b] 중 최소
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

print(-1) if distance >= INF else print(distance)
