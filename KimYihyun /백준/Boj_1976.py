# 여행가자
# https://www.acmicpc.net/problem/1976

n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


city = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            union_parent(i + 1, j + 1)


travel_plan = list(map(int, input().split()))
travel_set = set(travel_plan)  # 중복 제거


for i in travel_set:
    if find_parent(i) != find_parent(travel_plan[0]):
        print("NO")
        exit(0)

print("YES")
