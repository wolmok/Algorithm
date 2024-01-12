N, K = map(int, input().split())

res = 0
while N != 1:
    if N % K == 0: 
        N //= K
        res += 1
    else:
        N -= 1
        res += 1

print(res)
