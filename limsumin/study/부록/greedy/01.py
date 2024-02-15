# 모험가 길드
import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

n = int(input())
people = list(map(int, input().split()))

people = sorted(people)

cnt = 0
ans = 0
for person in people:
    cnt += 1

    if cnt >= person:
        ans += 1
        cnt = 0

print(ans)