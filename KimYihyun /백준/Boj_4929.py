# 수열 걷기
# https://www.acmicpc.net/problem/4929

while True:
    array1 = list(map(int, input().split()))
    if array1[0] == 0:
        break
    else:
        array2 = list(map(int, input().split()))
        first_array = array1[1:]
        second_array = array2[1:]
        sum_first, sum_second = 0, 0
        idx_first, idx_second = 0, 0
        result = 0

        # 첫 번째 원소 - 리스트의 길이
        while idx_first < array1[0] and idx_second < array2[0]:
            if first_array[idx_first] == second_array[idx_second]:
                result += max(sum_first, sum_second)  # 누적합을 먼저 더하고
                result += first_array[idx_first]  # 둘 중 아무 값이나 더해줌 (같으므로)
                sum_first, sum_second = 0, 0
                idx_first += 1
                idx_second += 1
            elif idx_first < array1[0] and first_array[idx_first] < second_array[idx_second]:
                # 범위 안에 있고, array1의 원소가 더 작을 경우
                sum_first += first_array[idx_first]
                idx_first += 1
            elif idx_second < array2[0] and second_array[idx_second] < first_array[idx_first]:
                # 범위 안에 있고, array2의 원소가 더 작을 경우
                sum_second += second_array[idx_second]
                idx_second += 1

        # 남은 부분 처리
        while idx_first < array1[0]:
            sum_first += first_array[idx_first]
            idx_first += 1

        while idx_second < array2[0]:
            sum_second += second_array[idx_second]
            idx_second += 1

        result += max(sum_first, sum_second)

        print(result)
