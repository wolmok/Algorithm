# 곱하기 혹은 더하기

import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

# 내 풀이 - 오답: 1 인 경우를 고려하지 않았음
# strs = input()
# ans = int(strs[1]) if int(strs[0]) == 0 else int(strs[0])
# isFirstZero = True if int(strs[0]) == 0 else False

# for i, s in enumerate(strs):
#     if int(s) == 0:
#         continue
#     else:
#         if isFirstZero and i == 1:
#             continue
#         elif i == 0:
#             continue
#         else:
#             ans *= int(s)

# print(ans)


# 답지 풀이
strs = input()

res = int(strs[0])

for i in range(1, len(strs)):
    num = int(strs[i])

    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)