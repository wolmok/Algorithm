# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

import sys
sys.stdin = open("limsumin/백준/input.txt","rt")

n = int(input())
a_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))


max_res = -int(1e9)
min_res = int(1e9)

def dfs(L, add, sub, mul, div, val):
    global max_res, min_res, res_list
    if L == n:
        max_res = max(max_res, val)
        min_res = min(min_res, val)
        return 

    if add:
        dfs(L+1, add-1, sub, mul, div, val + a_list[L])
    if sub:
        dfs(L+1, add, sub-1, mul, div, val - a_list[L]) 
    if mul:
        dfs(L+1, add, sub, mul-1, div, val * a_list[L]) 
    if div:
        dfs(L+1, add, sub, mul, div-1, int(val / a_list[L])) 


dfs(1, cal_list[0], cal_list[1], cal_list[2], cal_list[3], a_list[0])

print(max_res)
print(min_res)
