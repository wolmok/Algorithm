# 고정점 찾기
N = int(input())
numbers = list(map(int, input().split()))
fix = -1


def binary_search(fix):
    for i in range(len(numbers)):
        if (i == numbers[i]):
            fix = i
            return fix
    return fix


res = binary_search(fix)

print(res)
