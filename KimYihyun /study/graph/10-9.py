# 틀린 부분 답안 참고해 수정

from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)  # 진입차수를 모두 0으로 초기화

graph = [[] for i in range(v+1)]  # 간선 정보 그래프

class_time = [0] * (v+1)  # 각 강의 시간

for i in range(1, v+1):
    classes = list(map(int, input().split()))  # 강의 종류
    # 틀린 부분 여기부터
    class_time[i] = classes[0]  # 1번째 데이터 = 강의 시간 정보
    for x in classes[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    # 틀린 부분 여기까지 - (기존)값을 바꿔주는 방식->(변경)deepcopy 사용
    result = copy.deepcopy(class_time)
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + class_time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])


topology_sort()
