# 공유기 설치
# https://www.acmicpc.net/problem/2110

def count_routers(distance, houses, C):
    count = 1  # 첫 번째 집에는 항상 공유기를 설치한다고 가정

    current_house = houses[0]  # 현재 집의 위치
    for house in houses:
        if house - current_house >= distance:
            count += 1
            current_house = house

    return count >= C


def binary_search(houses, C):
    start = 1  # 최소 거리
    end = houses[-1] - houses[0]  # 최대 거리

    result = 0
    while start <= end:
        mid = (start + end) // 2

        if count_routers(mid, houses, C):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

result = binary_search(houses, C)
print(result)
