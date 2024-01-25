N = int(input())
A = list(map(int, input().split()))
# 이 부분을 [0] * (N+1)로 초기화해서 틀렸다.
# [1]로 초기화해주어야 하는 이유는 -> 혼자 가능할 경우의 길이가 1인 것을 고려해야 하기 때문
d = [1] * N

for i in range(N):
    for j in range(i):
        if (A[i] < A[j]):
            d[i] = max(d[i], d[j]+1)

print(max(d))
