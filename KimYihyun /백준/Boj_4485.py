# 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1


def dijkstra():
    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while queue:
        rupee, cur_x, cur_y = heapq.heappop(queue)

        if cur_x == N - 1 and cur_y == N - 1:
            print(f'Problem {count}: {distance[cur_x][cur_y]}')
            break

        for i in range(4):
            newX, newY = cur_x + dx[i], cur_y + dy[i]
            if 0 <= newX < N and 0 <= newY < N:
                newRupee = rupee + graph[newX][newY]
                if newRupee < distance[newX][newY]:
                    distance[newX][newY] = newRupee
                    heapq.heappush(queue, (newRupee, newX, newY))

    return distance[N-1][N-1]


while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    dijkstra()
    count += 1
