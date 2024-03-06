# 정렬된 수열에서 특정 수의 개수 구하기

N, X = map(int, input().split())  # 원소 개수 / 등장할 수
numbers = list(map(int, input().split()))  # 정렬된 배열 입력

def binary_search(numbers, target):
    start = 0
    end = len(numbers) - 1
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            # 찾은 값이 타겟과 일치할 때마다 카운트 증가
            count += 1
            # 찾은 값의 좌우로 탐색을 계속하여 중복된 값들도 카운트
            left = mid - 1
            right = mid + 1
            while left >= 0 and numbers[left] == target:
                count += 1
                left -= 1
            while right < len(numbers) and numbers[right] == target:
                count += 1
                right += 1
            break
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return count


result = binary_search(numbers, X)

if result > 0:
    print(result)
else:
    print(-1)
