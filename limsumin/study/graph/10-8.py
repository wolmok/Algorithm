# 도시 분할 계획
import sys

sys.stdin = open("limsumin/study/graph/input.txt","rt")

N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

graph = []

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(M):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph = sorted(graph, key= lambda x: x[0])

result = 0
last = 0

for cost, a, b in graph:
    pa = find_parent(a)
    pb = find_parent(b)

    if pa != pb:
        union_parent(a, b)
        result += cost
        last = cost


print(result - last)