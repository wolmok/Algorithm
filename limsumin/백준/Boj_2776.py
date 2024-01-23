# https://www.acmicpc.net/problem/2776
# 암기왕

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

def binary_search(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

T = int(input())

for _ in range(T):
    N = int(input())
    one_list = sorted(list(map(int, input().split())))

    M = int(input())
    two_list = list(map(int, input().split()))

    for item in two_list:
        res = binary_search(one_list, item, 0, len(one_list) - 1)
        
        if res != None:
            print(1)
        else:
            print(0)
    