# 좌표 정렬하기 2
# https://www.acmicpc.net/submit/11651

N = int(input())
ary = []

for i in range(N):
    xi, yi = map(int, input().split())
    ary.append([xi, yi])

sorted_ary = sorted(ary, key=lambda point: (point[1], point[0]))

for point in sorted_ary:
    # 주의 !!! sorted_ary(point[0], point[1]) 이런 식으로 쓰지 않기 
    print(point[0], point[1])
