# 개미 전사
# Bottom Up 방식

N = int(input())  # 식량창고의 개수
K = list(map(int, input()))  # 각 식량 창고에 저장된 식량 개수 정보
res = 0  # 결과를 저장할 변수 초기화

dp = [0] * N  # dp테이블 초기화

dp[0] = K[0]  # 첫 번째 원소 저장
dp[1] = max(K[0], K[1])  # 첫 번째 & 두 번째 원소 중 큰 값을 저장

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+K[i])

print(dp[N-1])  # N번째가 아니라 N - 1번째인 이유는 : index가 0부터 시작하기 때문 (틀린 이유)
