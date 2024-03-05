# 정수 삼각형
# https://www.acmicpc.net/problem/1932

# DFS 코드 - 시간 초과
N = int(input())  # 삼각형의 크기
triangle = []

for i in range(N):
    row = list(map(int, input().split()))
    triangle.append(row)


def dfs(row, col):
    # 삼각형의 마지막 줄에 도달한 경우
    if row == N - 1:
        return triangle[row][col]

    # 왼쪽과 오른쪽의 경우를 각각 계산
    left = dfs(row + 1, col)
    right = dfs(row + 1, col + 1)

    return max(left, right) + triangle[row][col]  # 더해서 합을 리턴


print(dfs(0, 0))

# dp 코드 - 통과
# 정수 삼각형
# https://www.acmicpc.net/problem/1932

N = int(input())  # 삼각형의 크기
triangle = []

for i in range(N):
    row = list(map(int, input().split()))
    triangle.append(row)

# 각 위치에서의 최대 합을 저장할 배열 초기화
dp = [[0] * N for _ in range(N)]


def dynamic_func():
    # 맨 아래 줄부터 시작
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if i == N - 1:
                dp[i][j] = triangle[i][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

    return dp[0][0]


# 최대 합 계산 및 출력
print(dynamic_func())
