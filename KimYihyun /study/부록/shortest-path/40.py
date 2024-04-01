# 최단 경로 - 숨바꼭질
import heapq

INF = int(1e9)

n, m = map(int, input().split())
# 시작 노드 -> 1번 헛간
start = 1
# 연결 노드 정보를 저장
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, cur = heapq.heappop(queue)
        if distance[cur] < dist:
            continue
        for i in graph[cur]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(start)

max_node = 0
max_dist = 0
res = []

for i in range(1, n + 1):
    if max_dist < distance[i]:
        max_node = i
        max_dist = distance[i]
        res = [max_node]
    elif max_dist == distance[i]:
        res.append(i)

print(max_node, max_dist, len(res))
