# 동전 게임
# https://www.acmicpc.net/problem/9079

T = int(input())


def flip(coins):
    # 동전의 상태 -> 문자열로 저장
    coin_list = set([''.join(row) for row in coins])  # 여기서 구글링함
    count = 0

    # all 동일한 상태라면
    if len(coin_list) == 1:
        return 0

    # for i in range(3):
    # 행
    #     if coins[0][i] == coins[1][i] == coins[2][i]:
    # 열
    #     if coins[i][0] == coins[i][1] == coins[i][2]:

    if count >= 0:
        return count
    else:
        return -1


for _ in range(T):
    coins = [input().split() for _ in range(3)]
    print(flip(coins))
