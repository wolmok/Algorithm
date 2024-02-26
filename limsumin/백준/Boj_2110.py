# https://www.acmicpc.net/problem/2110
# 공유기 설치

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

n, c = map(int, input().split())
wifis = []

for _ in range(n):
    wifis.append(int(input()))

wifis = sorted(wifis)

start = 1
end = wifis[-1] - wifis[0]
res = 0


while start <= end:
    mid = (end + start) // 2

    point = wifis[0]
    count = 1
    for i in range(1, len(wifis)):
        if wifis[i] >= point + mid:
            point = wifis[i]
            count += 1

    if count >= c:
        res = mid
        start = mid + 1
    else:
        end = mid -1

print(res)