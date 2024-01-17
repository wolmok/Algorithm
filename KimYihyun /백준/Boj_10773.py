# 제로
# https://www.acmicpc.net/problem/10773

K = int(input())

stack = []

for _ in range(K) :
    N = int(input())
    if N == 0 :
        stack.pop()
    else :
        stack.append(N)

print(sum(stack))
