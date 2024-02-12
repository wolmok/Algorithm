# 찾기 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 합치기 함수


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모 테이블 초기화

edges = []  # 간선 리스트
result = 0  # total cost 저장

for i in range(1, v+1):
    parent[i] = i  # 처음에는 자기 자신으로 초기화

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 비용 순으로 정렬
max_cost = 0  # 최고 비용이 드는 간선을 저장할 변수

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):  # 사이클 X인 경우
        union(parent, a, b)  # 합치기 수행
        result += cost  # 비용 합산
        max_cost = cost

print(result - max_cost)
