# 6-11.py

N = int(input())
array = []
for i in range(N):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda data: data[1])

for data in array:
    print(data[0], end=' ')
