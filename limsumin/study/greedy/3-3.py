# 숫자 카드 게임
import sys

sys.stdin = open("limsumin/study/greedy/input.txt","rt")

N, M = map(int, input().split())

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

min_ans = min(lst[0])

for i in range(1, len(lst)):
    min_val = min(lst[i])

    if min_val > min_ans:
        min_ans = min_val

print(min_ans)