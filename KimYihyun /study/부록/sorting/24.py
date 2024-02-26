# 안테나 (답 맞고 시간 초과)
# https://www.acmicpc.net/problem/18310

N = int(input())  # 집의 개수
houses = list(map(int, input().split()))  # 집의 위치
location = []

for antenna in houses:

    distance = 0
    for house in houses:
        distance += abs(antenna - house)

    location.append((antenna, distance))

min_distance = min(location, key=lambda x: x[1])


print(min_distance[0])
