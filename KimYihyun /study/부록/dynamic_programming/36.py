# 편집 거리
# 편집 거리 자체 알고리즘 참고
A = list(input())
B = list(input())

# 사용한 연산의 횟수를 최소로 카운트하는 것이라고 생각해서 이렇게 작성
# str_len = max(len(A), len(B))
# insert, remove, replace = 0, 0, 0 # 각 연산을 사용한 횟수를 초기화함

N = len(A)
M = len(B)

table = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N + 1):  # 테이블의 행으로 삽입
    table[i][0] = i

for j in range(1, M + 1):  # 테이블의 열로 삽입
    table[0][j] = j

# 여기서 서로 같은 문자를 만나는 경우는 - 0으로 카운팅됨

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if A[i - 1] == B[j - 1]:
            table[i][j] = table[i-1][j-1]
        else:
            table[i][j] = min(table[i][j-1], table[i-1]
                              [j-1], table[i-1][j]) + 1

print(table[N][M])
