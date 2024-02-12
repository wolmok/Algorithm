
# 크루스칼 알고리즘
def find_parent(parent, x):
    if parent[x] != x:  # 루트를 찾지 못한 경우
        parent[x] = find_parent(parent, parent[x])  # 찾을 때까지 재귀 호출
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 노드의 부모로 변경
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)  # 부모 테이블 초기화

edges = []  # 간선 리스트
result = 0  # 최종 간선 비용을 저장

for i in range(1, v+1):
    parent[i] = i  # 처음에는 자기 자신으로 테이블을 초기화

for _ in range(e):  # 간선 정보 입력받기
    a, b, cost = map(int, input().split())
    # 첫 번째 원소를 간선 비용으로 설정 - 비용순 정렬을 위함
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 X인 경우에 한해
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)  # 합치기 수행
        result += cost  # 최종 비용에 추가

print(result)
