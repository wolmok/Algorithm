# 최소 비용 구하기
# https://www.acmicpc.net/problem/1916
# 답 맞고 시간 초과 - input 방식 변경 + dictionary 사용해서 해결

import sys
import heapq
from collections import defaultdict

INF = int(1e9)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

# 도시, 버스 저장용 리스트
graph = defaultdict(list)

for i in range(m):
    a, b, price = map(int, sys.stdin.readline().split())  # 출발 도시 - 도착 도시 - 버스 비용
    graph[a].append((b, price))

start, end = map(int, sys.stdin.readline().split())  # 시작, 도착 도시

min_price = [INF]*(n+1)


def priceFunc(start):
    queue = [(0, start)]
    min_price[start] = 0

    # 비어있지 않은 동안
    while queue:
        # 현재까지 최소 비용 및 현재 도시의 번호
        cur_price, cur_city = heapq.heappop(queue)

        if min_price[cur_city] < cur_price:  # 최소 비용 다시 계산할 필요 없음
            continue

        for destination, price in graph[cur_city]:
            # 현재까지의 최소 비용 + 버스 비용 = 새로운 total 비용 갱신!
            total = min_price[cur_city] + price
            # 최소 비용 업데이트
            if min_price[destination] > total:
                min_price[destination] = total
                heapq.heappush(queue, (total, destination))


priceFunc(start)
print(min_price[end])
