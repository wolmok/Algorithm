# 최단 경로 - 간단한 다익스트라
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 / 간선 개수 입력받기
n, m = map(int, input().split())
start_node = int(input())  # 시작 노드 설정
graph = [[] for i in range(n+1)]  # 노드 정보 리스트

# n + 1까지로 초기화 : 노드 번호 == 인덱스로 하여 리스트로 바로 접근 가능하도록 처리
visited = [False] * (n + 1)  # 방문을 체크하는 리스트, True면 패스하고 넘기기
distance = [INF] * (n + 1)  # 각 거리를 무한대로 초기화, 후에 최단 거리를 입력

# 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    # a -> b로 가는 비용이 c
    graph[a].append((b, c))


def shortest_path(start):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        # 무한 -> 최단 거리로 갱신
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # 시작 노드에 연결된 간선에 접근
    # j - 간선 / j[0] - 도착 노드 / j[1] - 거리 정보
    for j in graph[start]:
        # 도착 노드와 거리에 대한 정보 갱신, 가장 헷갈렸던 부분
        distance[j[0]] = j[1]
    # 시작 노드 제외하고
    for i in range(n - 1):
        # 현재 노드와 가장 가까운 노드 방문
        cur = shortest_path()
        visited[cur] = True
        # 이외에 현재 노드와 연결된 노드를 순차 방문
        for j in graph[cur]:
            cost = distance[cur] + j[1]
            # 최단 거리가 더 짧아질 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start_node)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
