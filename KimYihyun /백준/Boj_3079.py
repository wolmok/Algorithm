# 입국심사
# https://www.acmicpc.net/problem/3079

# N : 입국심사대 개수
# M : 총 인원
N, M = map(int, input().split())
# Tk : 입국 심사에 소요되는 시간
Tk = list(map(int, input().split()))
# 오름차순으로 정렬, 따라서 0번째 인덱스가 소요되는 최소 시간
Tk.sort()

start, end = 0, M - 1
max_time = Tk[-1] * M

while start <= end:
    global total
    mid = (start + end) // 2
    for i in Tk:
        # total += i * M  ====> total을 어떻게 계산해야 할 지

print(total)
