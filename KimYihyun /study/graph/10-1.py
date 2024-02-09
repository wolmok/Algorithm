# union-find

# 루트 노드를 찾도록 호출되는 함수
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치며 번호가 작은 노드를 부모 노드로 설정


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # 노드/간선 개수 입력받기
parent = [0] * (v+1)  # 부모 노드를 저장하는 테이블을 생성

for i in range(1, v+1):
    parent[i] = i  # 처음에는 부모 테이블에 자기 자신을 저장하도록 설정

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)  # union 연산 수행


print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
