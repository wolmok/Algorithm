N, M, K = map(int, input().split())
numbers = sorted(list(map(int, input().split())), reverse=True)

# 가장 큰 수와 두 번째로 큰 수만 알면 됨
first = numbers[0] 
second = numbers[1] 

res = 0
while True:
    for i in range(K):
        if M == 0:
            break
        res += first
        M -= 1

    if M == 0:
        break
    res += second
    M -= 1

print(res)
