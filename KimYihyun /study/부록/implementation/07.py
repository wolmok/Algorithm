# 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

# 틀린 코드 - 원래 자릿수를 고려하지 않고 새로운 자릿수를 할당하는 방식이기 때문
# N = int(input())
# num = list(map(int, str(N)))
# print(num)

# res_list = []
# res = 0

# for i in range(0, len(num)):
#     res += num[i]

#     if i+1 == len(num)//2 or i+1 == len(num):  # 인덱스는 0부터 시작하므로
#         res_list.append(res)
#         res = 0


# if res_list[0] == res_list[1]:
#     print("LUCKY")
# else:
#     print("READY")

N = input()
num_length = len(N) // 2

left = list(map(int, N[:num_length]))
right = list(map(int, N[num_length:]))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
