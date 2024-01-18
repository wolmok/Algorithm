# 6-12.py

N, K = map(int, input().split())

arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

# 잘못 생각한 부분 ~
# data_A = input().split()
# data_B = input().split()

# # 각 배열에 data 삽입
# for i in range(N):
#     arrayA.append(data_A[i])
#     arrayB.append(data_B[i])
# 여기까지 ~

# 사용하기 쉽게 A를 오름차순으로 정렬
arrayA = sorted(arrayA)
# 사용하기 쉽게 B를 내림차순으로 정렬
arrayB = sorted(arrayB, reverse=True)

# 바꿔치기 연산
for i in range(K):
    # a의 가장 작은 원소
    # b의 가장 큰 원소 찾아 바꾼다
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        continue

print(sum(arrayA))
