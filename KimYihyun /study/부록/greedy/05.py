# 볼링공 고르기

N, M = map(int, input().split())  # 공 개수 / 공 최대 무게
K = list(map(int, input().split()))  # 각 볼링공의 무게

first_ball = 0
second_ball = 0
pairs = []

for first in range(N):
    for second in range(first+1, N):
        # 1번째 공 이후부터 선택해 중복 없도록
        first_ball = K[first]
        second_ball = K[second]
        if first_ball != second_ball:
            pairs.append((first_ball, second_ball))

print(len(pairs))
