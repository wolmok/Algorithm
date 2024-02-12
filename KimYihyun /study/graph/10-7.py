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


n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블을 초기화

# 처음에는 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0: # 팀 합치기 연산이 필요할 경우
        union(parent, a, b)
    elif oper == 1: # 같은 팀 여부 확인 연산이 필요할 경우
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
