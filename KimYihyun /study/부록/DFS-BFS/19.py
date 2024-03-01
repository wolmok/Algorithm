# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888

N = int(input())
num_list = list(map(int, input().split()))  # 주어지는 수열
flag_list = list(map(int, input().split()))  # 사칙연산 개수, + - x / 순서

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num_list[depth],
            plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_list[depth],
            plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_list[depth],
            plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_list[depth]),
            plus, minus, multiply, divide - 1)


dfs(1, num_list[0], flag_list[0], flag_list[1], flag_list[2], flag_list[3])
print(maximum)
print(minimum)
