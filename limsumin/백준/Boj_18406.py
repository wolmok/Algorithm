# https://www.acmicpc.net/problem/18406
# 럭키 스트레이트

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")
input = sys.stdin.readline

N = input()

mid = len(N) // 2

ans1 = 0
ans2 = 0
for i in range(mid):
    ans1 += int(N[i])

for j in range(mid, len(N)):
    ans2 += int(N[j])

if ans1 == ans2:
    print("LUCKY")
    exit(0)
else:
    print("READY")
    exit(0)