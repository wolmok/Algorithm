# 도로 포장
# https://www.acmicpc.net/problem/1162

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N, M, K = map(int, input().split())
K += 1

visited = [[False]*K for _ in range(N)]
distance = [[INF] * K for _ in range(N)]

queue = []
heapq.heappush(queue, (0, 0, K - 1))

road = [[] for _ in range(N)]

# 양방향 도로이므로
for _ in range(M):
    start, end, time = map(int, input().split())
    road[start - 1].append((end - 1, time))
    road[end - 1].append((start - 1, time))

# 서울은 0으로 초기화
for i in range(K):
    distance[0][i] = 0

while queue:
    res = heapq.heappop(h)
    cur_city, count = res[1], res[2]

    if visited[cur_city][count]:
        continue  # 이미 방문한 경우
    visited[cur_city][count] = True

    # 시간 부족으로 fail
