# 정수 삼각형
# https://www.acmicpc.net/problem/1932

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
