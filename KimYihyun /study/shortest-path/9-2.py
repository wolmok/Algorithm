# 최단 경로 - 개선된 다익스트라 - heapq 풀이
# heapq에 대한 사전 지식 X, 해설 보고 이해
import heapq

INF = int(1e9)

# 노드/간선 개수
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 연결된 노드의 정보
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 초기화
distance = [INF]*(n+1)

# 간선의 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b 비용:c
    graph[a].append((b, c))


def dijkstra(start):
    queue = []
    # 최단 경로 = 0으로 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:  # 큐가 비어있지 않은 동안
        # 최단 거리 노드를 꺼냄
        dist, now = heapq.heappop(queue)
        # 기존에 처리한 노드일 경우 - 계속 진행
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            # 최단 거리 갱신이 가능한 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 해당 거리 출력
    else:
        print(distance[i])
