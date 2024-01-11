# # 큰 수 만들기 
# # https://www.acmicpc.net/problem/16496
# N = int(input())
# numbers = list(map(int, input().split()))

# for i in range(N):
#     if numbers[i] == '0': 
#         #0을 포함하는 리스트일 경우
        
        
#     else: 
#         #0을 포함하지 않는 리스트일 경우
#         for j in range():

# 참고 링크
# https://imtech.tistory.com/15

N = int(input())
list = input().split()
cnt = 0

# 문자열로 만들어준 후에 버블 정렬을 통해 끝까지 검사
for i in range(N-1, 0, -1): 
    for j in range(i):
        if int(list[j] + list[j+1]) > int(list[j+1] + list[j]):
            pass
        else:
            list[j], list[j+1] = list[j+1], list[j]

for l in list: # 다 0일 경우 0 하나만 출력
    if l == "0":
        cnt += 1

if cnt == N:
    print(0)
else:
    print(''.join(list))
