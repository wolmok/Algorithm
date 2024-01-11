N, M = map(int, input().split())

res = 0

for i in range(N):
    # N번 반복 수행하며 값을 입력받고
    arr = list(map(int, input().split()))  
    # arr에서 최솟값을 저장한 후 
    min = min(arr)
    # 가장 큰 값을 res에 저장하고 출력
    res = max(min, res)
    
print(res)
