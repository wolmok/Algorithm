# 떡볶이 떡 만들기
N, M = map(int, input().split())  # 떡의 개수 / 요청한 떡의 길이
array = list(map(int, input().split()))  # 개별 떡의 높이

start = 0
end = max(array)
answer = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2  # 현재 10
    for i in range(N):
        if array[i] > mid:
            total += array[i] - mid
    if (total < M):  # 떡의 길이가 모자르면
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
print(answer)
