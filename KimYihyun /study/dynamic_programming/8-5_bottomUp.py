# 1로 만들기 - Bottom Up 방식 : 반복문을 활용해 작은 문제 -> 큰 문제 순으로 해결한다.

X = int(input())
dp = [0] * 30001  # 테이블 초기화, 연산 횟수를 저장해야 하므로 1 크게 설정

for i in range(2, X + 1):
    # 1을 빼는 가장 작은 문제를 해결
    dp[i] = dp[i - 1] + 1

    # 큰 문제 해결 시작
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)  # 횟수니까 dp[i//2+1]이 아님
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[X])
