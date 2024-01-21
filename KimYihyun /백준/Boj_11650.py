# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

N = int(input())
ary = []

for i in range(N):
    xi, yi = map(int, input().split())
    ary.append([xi, yi])

result_ary = sorted(ary, key=lambda cur: (cur[0], cur[1]))
for cur in result_ary:
    print(cur[0], cur[1])
