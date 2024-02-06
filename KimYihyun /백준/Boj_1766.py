# 문제집 - 위상정렬
# https://www.acmicpc.net/problem/1766

import sys
import heapq

N, M = map(int, input().split())
# 문제 푸는 순서를 저장
problem = [[] for i in range(N + 1)]
# 각 문제의 진입 차수
in_degree = [0 for i in range(N + 1)]
heap = []
res = []

# 문제 푸는 순서를 입력받고 진입 차수를 계산
for i in range(M):
    A, B = map(int, input().split())
    problem[A].append(B)
    in_degree[B] += 1

# 진입 차수가 0인 경우에 힙에 추가
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(heap, i)


# 비어있지 않은 동안 진입 차수 감소 with 뽑은 문제를 결과 리스트에 추가
while heap:
    cur = heapq.heappop(heap)
    res.append(cur)
    for j in problem[cur]:
        in_degree[j] -= 1
        # 진입 차수가 0이라면 다시 힙에 추가 => 풀 수 있게 된 문제
        # 따라서 다음에 처리할 수 있는 문제가 됨
        if in_degree[j] == 0:
            heapq.heappush(heap, j)

# 결과 출력
for i in res:
    print(i, end=' ')
