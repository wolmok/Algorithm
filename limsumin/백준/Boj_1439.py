# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439 


import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

s = input()

cnt = 0

for i in range(len(s) -1):
    if s[i] != s[i+1]:
        cnt += 1

print((cnt + 1) // 2)