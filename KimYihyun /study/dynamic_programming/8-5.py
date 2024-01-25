X = int(input())
# DP 테이블 초기화
d = [0] * (X+1)

for i in range(2, X+1):

    # 1을 빼는 경우를 먼저 고려
    d[i] = d[i-1] + 1
    # 나누어 떨어지는 경우 1을 뺐던 결과와 비교,
    # 작은 값을 d[i]에 저장
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[X])
