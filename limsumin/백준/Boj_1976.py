# 여행 가자
# https://www.acmicpc.net/problem/1976

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())
m = int(input())

parent = [0] * (n+1)
graph = []

for i in range(1, n+1):
    parent[i] = i

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

for i in range(n):  
    row = list(map(int, input().split()))
    graph.append(row)

    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i + 1, j + 1)

travel_list = list(map(int, input().split()))
travel_set = set(travel_list)

p = find_parent(travel_list[0])

for i in travel_set:
    pi = find_parent(i)

    if pi != p:
        print("NO")
        exit(0)

print("YES")
