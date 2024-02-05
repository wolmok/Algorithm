# 전보
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
min_distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문 X 노드 중에서, 최단거리 노드를 반환


def min_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if min_distance[i] < min_value and not visited[i]:
            min_value = min_distance[i]
            index = i
    return index


def message(start):
    # 시작 노드에 대해서 초기화
    min_distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        min_distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = min_node()
        visited[now] = True
        # 연결된 기타 노드 점검?
        for j in graph[now]:
            cost = min_distance[now] + j[1]
            # 더 짧은 거리인 경우 갱신
            if cost < min_distance[j[0]]:
                min_distance[j[0]] = cost


message(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 시작 노드 자체는 거리를 출력하지 않음
    if i == start:
        continue
    # 도달할 수 없는 경우 무한 출력
    if min_distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(min_distance[i])
