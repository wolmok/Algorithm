# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq

N = int(input())
cards = []  # 입력받을 배열

for i in range(N):
    heapq.heappush(cards, int(input()))

total_cost = 0

# 카드 묶음이 하나 남을 때까지 반복
while len(cards) > 1:
    # 가장 작은 두 묶음 선택
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    # 두 묶음을 합쳐서 새로운 묶음 생성
    new_bundle = a + b
    total_cost += new_bundle  # 합칠 때마다 비용 추가
    # 새로운 묶음을 다시 heapq에 삽입
    heapq.heappush(cards, new_bundle)

print(total_cost)
