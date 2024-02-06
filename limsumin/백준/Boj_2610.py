# https://www.acmicpc.net/problem/2610
# 참고: https://steady-coding.tistory.com/104
# 회의준비 
# union-find, 플로이드-워셜 알고리즘 사용

import sys
from collections import defaultdict

sys.stdin = open("limsumin/백준/input.txt","rt")

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
parent = [0] * (N+1)

# union-find algorithm 구현
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b= map(int, input().split())
    union(a, b)
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

conference = defaultdict(lambda: [N + 1, INF])
# 각 인덱스별 graph 의 최댓값이 가장 작은 index 찾아주기
for i in range(1, N + 1):
    f = find_parent(i)
    maximum_shortest_path = max(graph[i][j] if graph[i][j] != INF else 0 for j in range(1, N + 1))
    # print(maximum_shortest_path)
    conference[f] = min(conference[f], [i, maximum_shortest_path], key= lambda x: x[1])


# Sort and print the result
sorted_conference = sorted(conference.values(), key=lambda x: x[0])
print(len(sorted_conference))
for rep, _ in sorted_conference:
    print(rep)