def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 경로를 따라 올라가며 부모를 찾는 것이 아니라, 노드 x에서 루트까지 경로상 모든 노드의 부모를 직접 루트로 설정
# 정말 루트 노드를 찾을 때까지 재귀적 호출
