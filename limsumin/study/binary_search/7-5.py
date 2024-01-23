# 부품 찾기

import sys

sys.stdin = open("limsumin/study/binary_search/input.txt","rt")

N = int(input())
all_list = list(map(int, input().split()))
M = int(input())
needed_list = list(map(int, input().split()))

all_list = sorted(all_list)

# 이진 탐색
def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return False

for element in needed_list:
    res = binary_search(all_list, element, 0, len(all_list) - 1)

    if not res:
        print('no', end=' ')
    else:
        print('yes', end=' ')


