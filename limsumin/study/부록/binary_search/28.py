# 고정점 찾기
# 이진탐색

import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

n = int(input())
point_list = list(map(int, input().split()))

ans = -1
start = 0
end = len(point_list) - 1

while start <= end:
    mid = (start + end) // 2

    if point_list[mid] == mid:
        ans = mid
        break
    elif point_list[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

print(ans)