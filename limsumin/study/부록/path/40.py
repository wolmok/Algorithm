# 숨바꼭질
import sys
sys.stdin = open("limsumin/study/부록/input.txt","rt")

n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i- 1][j - 1] = 1
    graph[j- 1][i - 1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

num = 0
dist = -int(1e9)
count_same = 0

for j in range(n):
    print(graph[0][j])
    if graph[0][j] == 0:
        continue
    elif dist < graph[0][j]:
        dist = graph[0][j]
        num = j + 1
        # count_same += 1
    elif dist == graph[0][j]:
        count_same += 1 

print(num, dist, count_same)