# 찾기
def find_parent(parent, x):
    if parent[x] != x:  # 루트를 찾지 못한 경우
        parent[x] = find_parent(parent, parent[x])  # 찾을 때까지 재귀 호출
    return parent[x]

# 합치기


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

for i in range(1, v+1):
    parent[i] = i  # 처음에는 자기 자신으로 부모 테이블 초기화

cycle = False

for i in range(e):
    # 간선 개수만큼 돌면서
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):  # 사이클 O인 경우
        cycle = True
        break  # 종료
    else:
        union_parent(parent, a, b)  # 사이클 X인 경우 합치기 수행

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
