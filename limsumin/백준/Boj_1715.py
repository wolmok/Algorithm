# https://www.acmicpc.net/problem/1715
# 카드 정렬하기

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

import heapq

n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
    exit(0)

ans = 0

while len(cards) > 1:
    cur1 = heapq.heappop(cards)
    cur2 = heapq.heappop(cards)
    ans += cur1 + cur2
    heapq.heappush(cards, cur1 + cur2) # 큐를 정렬하여 새로운 묶음이 항상 작은 순서대로 정렬되도록 함

print(ans)
