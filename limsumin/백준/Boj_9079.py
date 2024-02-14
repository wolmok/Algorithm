# 동전 게임
# https://www.acmicpc.net/problem/9079

import sys
from collections import deque

sys.stdin = open("limsumin/백준/input.txt", "rt")  

visited = [False] * 512
coins = [[0] * 3 for _ in range(3)]

def isSame():
    first = coins[0][0]
    for i in range(3):
        for j in range(3):
            if first != coins[i][j]:
                return False
            
    return True

def pointToInt():
    now = 0
    for i in range(3):
        for j in range(3):
            now = now * 2 + coins[i][j]

    return now

def IntToPoint(num):
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            coins[i][j] = num % 2
            num //= 2

def column_change(col):
    for i in range(3):
        val = 1 if coins[i][col] == 0 else 0
        coins[i][col] = val

def row_change(row):
    for i in range(3):
        val = 1 if coins[row][i] == 0 else 0
        coins[row][i] = val

def cross_change(cross):
    for i in range(3):
        if cross == 0:
            val = 1 if coins[i][i] == 0 else 0
            coins[i][i] = val
        else:
            val = 1 if coins[i][2-i] == 0 else 0
            coins[i][2-i] = val

def game():
    shown_list = []
    queue = deque()

    start = pointToInt()
    queue.append([0, start])
    visited[start] = True

    while queue:
        count, point = queue.popleft()

        IntToPoint(point)

        if isSame():
            return count
        
        for i in range(3):
            column_change(i)
            next = pointToInt()
            if not visited[next]:
                visited[next] = True
                queue.append([count + 1, next])
            column_change(i)

        for i in range(3):
            row_change(i)
            next = pointToInt()
            if not visited[next]:
                visited[next] = True
                queue.append([count + 1, next])
            row_change(i)

        for i in range(2):
            cross_change(i)
            next = pointToInt()
            if not visited[next]:
                visited[next] = True
                queue.append([count + 1, next])
            cross_change(i)

    return -1
        


T = int(input())
for _ in range(T):
    coins = []
    visited = [False] * 512
    for _ in range(3):
        a_list = []
        a = list(map(str, input().split()))
        for item in a:
            if item == "H":
                a_list.append(1)
            else:
                a_list.append(0)
        coins.append(a_list)

    print(game())
