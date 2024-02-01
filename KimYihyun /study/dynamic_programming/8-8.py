# 효율적인 화폐 구성
n, m = map(int, input().split()) 
array = [] 
for i in range(n):
  array.append(int(input())) 

d = [10001] * (m + 1) 

d[0] = 0
for i in range(n): # array 안에 저장된 화폐 개수만큼 반복
  # 화폐 단위보다 작은 경우 계산 불가하므로 array[i]부터 시작
  for j in range(array[i], m + 1): 
    if d[j - array[i]] != 10001: # 초기값 그대로가 아닌 경우
      # 해당 값과 이전에 계산한 값 중 최소값을 저장
      d[j] = min(d[j], d[j - array[i]] + 1) 

# 만들 수 없는 수인 경우
if d[m] == 10001:
  print(-1)
else:
  print(d[m]) 
