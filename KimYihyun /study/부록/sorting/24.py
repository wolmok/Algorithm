# 안테나
# https://www.acmicpc.net/problem/18310

N = int(input())  # 집의 개수
houses = list(map(int, input().split()))  # 집의 위치

houses.sort() 

# 안테나를 중간에 설치하는 경우
if N % 2 == 0:
    antenna_position = houses[N // 2 - 1]
else:
    antenna_position = houses[N // 2]

print(antenna_position)
