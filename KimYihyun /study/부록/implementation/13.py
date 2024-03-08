# 치킨 배달
# https://www.acmicpc.net/problem/15686
# 틀린 이유 : itertools - combinations 활용 관련

from itertools import combinations

N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))

result = 1e9
house = []  # 집
chicken_store = []  # 치킨집

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken_store.append([i, j])

for chicken in combinations(chicken_store, M):  # m개의 치킨집까지의 모든 조합을 계산
    temp = 0
    for h in house:
        house_between = 1e9   # 집 ~ 치킨집 거리
        for j in range(M):
            house_between = min(house_between, abs(
                h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1]))
        temp += house_between
    result = min(result, temp)

print(result)
