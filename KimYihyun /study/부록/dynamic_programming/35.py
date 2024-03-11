# 못생긴 수
# 틀린 코드 주석
N = int(input())
ugly_num = [0] * 1001

ugly_num[0] = 1
# res = []

# for i in range(1, N):
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#         ugly_num[i] = True
#         res.append(i)

# print(res[-1])  # 항상 마지막 요소인 N을 담고 있도록

i2 = i3 = i5 = 0
next_2, next_3, next_5 = 2, 3, 5

for i in range(1, N):
  ugly_num[i] = min(next_2, next_3, next_4)
  if ugly_num[i] == next_2:
    i2 += 1
    next_2 = ugly_num[i2] * 2
  elif ugly_num[i] == next_3:
    i3 += 1
    next_3 = ugly_num[i3] * 3
  elif ugly_num[i] == next_5:
    i5 += 1
    next_5 = ugly_num[i5] * 5

print(ugly_num(N-1))
    

