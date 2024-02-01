# 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

T = int(input())


def cal(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return cal(num-1) + cal(num-2) + cal(num-3)


for i in range(T):
    num = int(input())
    print(cal(num))
