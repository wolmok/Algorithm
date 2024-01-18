# 위에서 아래로 

import sys

sys.stdin = open("limsumin/study/sort/input.txt","rt")

N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list = sorted(num_list, reverse= True)

for num in num_list:
    print(num, end= ' ')