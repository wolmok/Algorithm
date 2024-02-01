# 플로이드-워셜 알고리즘 구현

import sys

sys.stdin = open("limsumin/study/path/input.txt","rt")

INF = int(1e9)

N = int(input())
M = int(input())

# 2차원 리스트 선언
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신으로 가는 길의 비용은 0 으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# 간선 정보 입력 받고 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print("INFINITY", end= " ")
        else:
            print(graph[i][j], end= " ")

    print()