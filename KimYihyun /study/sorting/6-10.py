# 6-10.py

N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

array = sorted(array, reverse=True)

for j in range(len(array)):
    print(array[j], end=' ')
