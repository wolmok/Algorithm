# 고정점 찾기 : 시간복잡도를 고려해 수정
def binary_search(numbers):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == mid:
            return mid
        elif numbers[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


N = int(input())
numbers = list(map(int, input().split()))

res = binary_search(numbers)

print(res)
