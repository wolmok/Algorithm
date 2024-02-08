# 팀 결성

import sys

sys.stdin = open("limsumin/study/graph/input.txt","rt")

N, M = map(int, input().split())

parent = [i for i in range(0, N+1)]

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

for i in range(M):
    d, a, b = map(int, input().split())

    if d == 0:
        union_parent(a, b)
    else:
        pa = find_parent(a)
        pb =find_parent(b)

        if pa == pb:
            print("YES")
        else:
            print("NO")
