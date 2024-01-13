# 더하기
# https://www.acmicpc.net/problem/9085

# 테스트 케이스 개수
T = int(input())

for i in range(T):
    # 합을 출력할 변수 선언 및 초기화
    sum = 0
    # 자연수의 개수
    N = int(input())
    # N개의 자연수
    numbers = list(map(int, input().split()))
    for j in range(N):
        sum += numbers[j]
    #합 출력
    print(sum)

