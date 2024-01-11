# 구현: 상하좌우

import sys

sys.stdin = open("limsumin/study/imple/input.txt","rt")

N = int(input())
dir_list = list(map(str, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cur = (1, 1)

for d in dir_list:
    # 방향별로 dx, dy 를 사용할 인덱스를 지정
    idx = 0
    if d == "R":
        idx = 1
    elif d == "U":
        idx = 2
    else:
        idx = 3

    # 이동할 좌표 계산
    nx, ny = cur[0] + dx[idx], cur[1] + dy[idx]
    
    # 이동할 좌표 유효성 검사
    if nx <= 0 or nx > N or ny <= 0 or ny > N:
        continue
    else:
        cur = (nx, ny)

print("{} {}".format(cur[0], cur[1]))