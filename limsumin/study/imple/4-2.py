# 시각

import sys

sys.stdin = open("limsumin/study/imple/input.txt","rt")

N = int(input())
count = 0

# 시간, 분, 초 함께 확인
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count += 1  

print(count)