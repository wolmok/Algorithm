# 정렬된 배열에서 특정 개수 구하기

import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

res = -1

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == x:
        while arr[left] != x:
            left += 1
        while arr[right] != x:
            right -= 1
        res = right - left + 1
        break

    else:
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1


print(res)
