# https://www.acmicpc.net/problem/4929
# 수열 걷기 - 이분 탐색 안써도 되는 듯..?

import sys

sys.stdin = open("limsumin/백준/input.txt","rt")

while True:
    first_lst = list(map(int, input().split()))
    if first_lst[0] == 0:
        break
    else:
        sec_lst = list(map(int, input().split()))
        f_element = first_lst[1:]
        s_element = sec_lst[1:]

        result = 0
        f_sum, s_sum = 0, 0
        f_idx, s_idx = 0, 0

        while f_idx < first_lst[0] and s_idx < sec_lst[0]:
            if f_element[f_idx] == s_element[s_idx]:
                result += max(f_sum, s_sum)
                result += f_element[f_idx]
                f_sum, s_sum = 0, 0
                f_idx += 1
                s_idx += 1
            elif f_idx < first_lst[0] and f_element[f_idx] < s_element[s_idx]: # 수열 1 의 값이 수열 2의 값보다 작다면 수열 1의 누적합을 증가
                f_sum += f_element[f_idx]
                f_idx += 1
            elif s_idx < sec_lst[0] and s_element[s_idx] < f_element[f_idx]:
                s_sum += s_element[s_idx]
                s_idx += 1

        while f_idx < first_lst[0]:
            f_sum += f_element[f_idx]
            f_idx += 1
        while s_idx < sec_lst[0]:
            s_sum += s_element[s_idx]
            s_idx += 1
        
        result += max(f_sum, s_sum)

        print(result)
            


