# 퇴사2
# https://www.acmicpc.net/problem/15486
# 오답 제출 후 재풀이

n = int(input())
# (걸리는 시간, 버는 돈) 형태의 리스트
li = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)
max_price = 0

for i in range(n):
    # 이전의 최대 금액과 현재 저장된 돈 비교
    max_price = max(max_price, dp[i])
    # 일이 끝나는 날
    final_day = i + li[i][0]
    if final_day <= n:
        dp[final_day] = max(max_price + li[i][1], dp[final_day])

# 최댓값 출력
print(max(dp))
