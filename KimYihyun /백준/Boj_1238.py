# 파티
# https://www.acmicpc.net/problem/1238

import heapq

INF = int(1e9)
N, M, X = map(int, input().split())
info = [[] for _ in range(N+1)]

res = [[]]
times = []


def max_time(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in info[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


for i in range(1, M+1):
    # 시작점/끝점/소요시간
    start, end, time = list(map(int, input().split()))
    info[start].append((end, time))

for i in range(1, N+1):
    distance = [INF] * (N+1)  # 반복문이 돌 때마다 초기화
    res.append(max_time(i))

for j in range(1, N+1):
    times.append(res[j][X] + res[X][j])  # 집-파티까지 / 파티-집까지 최단 경로 저장


print(max(times))
