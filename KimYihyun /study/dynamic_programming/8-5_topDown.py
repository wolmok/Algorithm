# 1로 만들기 - Top Down 방식 : 재귀함수를 사용해 큰 문제 사용에 작은 문제를 호출해 해결한다.

X = int(input())
dp = [0] * 30001  # 테이블 초기화, 연산 횟수를 저장해야 하므로 1 크게 설정

# 작은 문제를 해결하기 위한 재귀 함수 정의


def make_one(X):
    # 1인 경우 연산 횟수 0번 그대로 반환
    if X == 1:
        return 0
    # 이미 계산해서 값이 들어있는 경우 그대로 리턴
    if dp[X] != 0:
        return dp[X]

    # ***중요***
    # 나누어 떨어지지 않는 경우에 해당 횟수가 최솟값으로 설정되지 않도록 큰 수로 세팅
    five = three = two = 99999

    if X % 5 == 0:
        five = make_one(X // 5)
    if X % 3 == 0:
        three = make_one(X // 3)
    if X % 2 == 0:
        two = make_one(X // 2)

    # 최솟값을 구해 리턴
    dp[X] = min(five, three, two, make_one(X-1)) + 1
    return dp[X]


# 함수 리턴값을 출력
print(make_one(X))
