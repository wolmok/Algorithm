# 1이 될 때까지
import sys

sys.stdin = open("limsumin/study/greedy/input.txt","rt")

N, K = map(int, input().split())

count = 0

while N >= K:
    while N % K != 0: # 배수가 아닐 때
        N -= 1
        count += 1
    
    N /= K # 배수일 때는 나누어주면 됨
    count += 1

while N > 1: # N 이 K 보다 작지만 1 이 아닌 경우
    N -= 1
    count += 1

print(count)