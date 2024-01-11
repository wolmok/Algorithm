# 큰 수의 법칙
import sys

sys.stdin = open("limsumin/study/greedy/input.txt","rt")

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# numbers 를 내림차순으로 정렬
numbers = sorted(numbers, reverse= True)

# 첫번째로 큰 값과 두번째로 큰 값 변수로 저장
highest = numbers[0]
second = numbers[1]

sum = 0 # 전체 합
count = 0 # 더한 횟수 카운트
while True: 
    for i in range(K): # 최댓갑 3번 더하는 연산
        if count == M:
            break
        sum += highest
        count += 1
    
    if count == M:
        break
    sum += second # 두번째로 큰 값 1번 더하는 연산
    count += 1

print(sum)