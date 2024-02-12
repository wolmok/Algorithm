# 위상 정렬 - 방향에 거스르지 않도록 모든 노드를 순서대로 나열하는 정렬 알고리즘 (선후 관계가 있다는 전제)
# 진입차수를 선행적으로 고려

from collections import deque

v, e = map(int, input().split())  # 노드, 간선 개수 입력받기
indegree = [0] * (v+1)  # 모든 노드의 진입차수를 0으로 우선 초기화

# 각 노드에 연결된 간선 정보를 담을 그래프 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):  # 모든 간선 정보 입력
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b로 이동 가능
    indegree[b] += 1  # 간선의 진입 차수를 1 증가


def topology_sort():
    result = []  # 수행 결과를 담을 리스트를 초기화
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)  # 진입차수가 0인 노드를 큐에 삽입
    while q:
        now = q.popleft()  # 큐가 빌 때까지 원소를 하나씩 꺼내서
        result.append(now)  # 현재 원소를 결과 리스트에 삽입
        for i in graph[now]:
            indegree[i] -= 1  # 진입 차수를 조정
            if indegree[i] == 0:  # 이 과정에서 진입차수가 0이 되는 노드는
                q.append(i)  # 새롭게 큐에 삽입 후 위 과정을 반복

    # 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()
