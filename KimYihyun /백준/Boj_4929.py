# 수열 걷기
# https://www.acmicpc.net/problem/4929

sum_first = 0  # 첫 번째 수열에서 시작한 합
sum_second = 0  # 두 번째 수열에서 시작한 합
res = 0  # 최종 결과


def sequence(array1, array2):
    global len_ary
    if len(array1) > len(array2):
        len_ary = len(array1)
    elif len(array1) < len(array2):
        len_ary = len(array2)
    else:
        len_ary = len(array1)  # 어떤 리스트의 길이만큼 반복해도 상관 없음
    for i in range(len_ary):
        # 다를 경우 그냥 더함
        if array1[i] != array2[i]:
            sum_first += array1[i]
            sum_second += array2[i]
        else:  # 같아지면
            mid = (array1[i] + array2[i]) // 2
            if array1[i + 1] > mid:
                sum_first += array2[i]
                sum_second += array2[i]
            elif array2[i + 1] < mid:
                sum_first += array1[i]
                sum_second += array1[i]
    if sum_first > sum_second:
        res = sum_first
    else:
        res = sum_second  # 만약 같더라도 상관 없음
    print("res:", res)


while True:
    array1 = list(map(int, input().split()))
    if array1[0] == 0:
        break
    else:
        array2 = list(map(int, input().split()))
        # print(array1, array2)
        # 1번째 원소부터 저장한 리스트
        first_array = array1[1:]
        second_array = array2[1:]
        # print(first_array, second_array)


print(sequence(first_array, second_array))
