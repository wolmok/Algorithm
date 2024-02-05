# 최단 경로 - 플로이드 워셜
INF = int(1e9)

n = int(input())  # 노드 정보
m = int(input())  # 간선 정보

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기-자기 -> 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선정보를 받아 그래프정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 여러 정보 중 최솟값을 넣어주기
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for p in range(1, n+1):
        for q in range(1, n+1):
            graph[p][q] = min(graph[p][q], graph[p][k]+graph[k][q])

# 결과
for i in range(1, n+1):
    for j in range(1, n+1):
        # 도달하지 못하면
        if graph[i][j] == INF:
            print(0, end=' ')
        # 도달할 수 있으면 -> 거리를 출력
        else:
            print(graph[i][j], end=' ')
    print()
