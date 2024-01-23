# 떡볶이 떡 만들기

import sys

sys.stdin = open("limsumin/study/binary_search/input.txt","rt")

N, M = map(int, input().split())
len_list = list(map(int, input().split()))


start = 0
end = max(len_list)
answer = 0

while start <= end:
    mid = (start + end) // 2

    res = 0
    for item in len_list:
        if item > mid:
            res += (item - mid)
    
    if res < M:
        end = mid - 1
    else:
        answer = max(answer, mid)
        start = mid + 1

print(answer)