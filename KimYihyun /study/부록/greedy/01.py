# 모험가 길드

N = int(input())  # 모험가의 수
ary = list(map(int, input().split()))  # 각 모험가의 공포도

ary.sort()  # 공포도 정렬
res = 0
cnt = 0

for i in ary:
    cnt += 1
    if (cnt >= i):
        res += 1
        cnt = 0  # 카운트 초기화

print(res)
