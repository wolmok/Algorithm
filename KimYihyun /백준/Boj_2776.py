# 테스트 케이스의 개수 입력
T = int(input())


def search_answer(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for _ in range(T):
    # 수첩 1에 적어놓은 정수의 개수
    N = int(input())
    array1 = list(map(int, input().split()))
    # 수첩 2에 적어놓은 정수의 개수
    M = int(input())
    array2 = list(map(int, input().split()))
    array1.sort()


for i in array2:
    start = 0
    end = M - 1
    print(search_answer(array1, i, start, end))
