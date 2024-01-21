N, k = map(int, input().split())
array = list(map(int, input().split()))

# 큰 순서대로 - 내림차순으로 정렬
array.sort(reverse=True)

# index는 0부터 시작하므로, k-1
print(array[k-1])
