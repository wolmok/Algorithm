# 왕실의 나이트

import sys

sys.stdin = open("limsumin/study/imple/input.txt","rt")

dir = input()

# 시작열, 시작행 구하기
start_col, start_row = int(ord(dir[0]) - 96), int(dir[1])

# 이동할 수 있는 direction 정의
direction = [(-2, 1), (2, -1), (2, 1), (-2, -1), (-1, 2), (1, -2), (1, 2), (-1, -2)]

# count 
count = 0

for d in direction:
    print(d)
    nx, ny = start_col + d[0], start_row + d[1]

    if nx >= 1 and nx <= 8 and ny >=1 and ny <= 8:
        count += 1
print(count)