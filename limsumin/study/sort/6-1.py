# 선택 정렬 구현
# 시간 복잡도: O(n^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    minimum = array[i]
    minimum_idx = i

    for j in range(i + 1, len(array)):
        if minimum > array[j]:
            minimum = array[j]
            minimum_idx = j
    
    # swap element
    array[i], array[minimum_idx] = array[minimum_idx], array[i] 

print(array)
