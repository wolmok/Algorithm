# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 앞 원소가 뒤 원소보다 클 때는 swap 해줘야 함
            array[j], array[j - 1] = array[j -1], array[j]
        else: # 그렇지 않은 경우는 for 문을 더 돌릴 필요가 없음
            break

print(array)