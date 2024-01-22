# 입국심사
# https://www.acmicpc.net/problem/3079

# N : 입국심사대 개수
# M : 총 인원
N, M = map(int, input().split())
# Tk : 입국 심사에 소요되는 시간
Tk = []
for _ in range(N):
    Tk.append(int(input()))
# 오름차순으로 정렬, 따라서 0번째 인덱스가 소요되는 최소 시간
Tk = sorted(Tk)

start = Tk[0]
end = Tk[-1] * M
res = float('inf')

while start <= end:
    global total
    total = 0
    mid = (start + end) // 2
    for t in Tk:
        # mid라는 시간 동안 심사 가능한 인원 수 파악
        total += (mid // t)

    # 만약 mid 시간 동안 M명을 심사하고 남는다면 끝점을 이동
    if (total >= M):
        end = mid - 1
        res = min(res, mid)
    # 아니라면 시작점을 이동
    else:
        start = mid + 1
print(res)
