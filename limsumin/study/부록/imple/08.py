# 문자열 재정렬 
import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

S = input()
alpha_list = []
integer_ans = 0
for s in S:
    if 65 <= ord(s) <= 90:
        alpha_list.append(s)
    else:
        integer_ans += int(s)

alpha_list = sorted(alpha_list)
str_ans = str(integer_ans)

alpha_list.append(str_ans)

print(''.join(alpha_list))