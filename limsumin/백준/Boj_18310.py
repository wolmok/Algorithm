# https://www.acmicpc.net/problem/18310
# 안테나

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())
houses = list(map(int, input().split()))
houses = sorted(houses)

print(houses[(n-1) // 2])