change = [500, 100, 50, 10]

N = 1260
count = 0

for c in change:
    count += N // c
    N %= c

print(count)