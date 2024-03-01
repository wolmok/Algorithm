# 금광
# 행 기준으로 보고 구현해서 틀림 .. ^^ + index range issue
T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    n, m = map(int, input().split())  # 세로 * 가로 금광 크기
    gold_list = list(map(int, input().split()))  # 금의 개수
    gold_map = []

    for i in range(n):
        gold_map.append(gold_list[i*m: i*m+m])  # 금광의 정보 추가

    res = 0
    for j in range(1, m):
        for i in range(n):
            # 좌측 상단 X?
            if (i == 0):
                gold_map[i][j] += max(gold_map[i][j-1], gold_map[i+1][j-1])
            # 좌측 하단 X?
            elif (i == n - 1):
                gold_map[i][j] += max(gold_map[i-1][j-1], gold_map[i][j-1])
            # 좌측 상단/하단 모두 X?
            else:
                gold_map[i][j] += max(gold_map[i-1][j-1],
                                      gold_map[i][j-1], gold_map[i+1][j-1])

    # 최댓값 골라서 출력
    for i in range(n):
        res = max(res, gold_map[i][m - 1])

    print(res)
