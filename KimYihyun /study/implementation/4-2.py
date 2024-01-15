# 시각
N = int(input())
count = 0

for h in range(N + 1):  # 시
    for m in range(60):  # 분
        for s in range(60):  # 초
            time = str(h)+str(m)+str(s)
            if '3' in time:  # 3이 포함된 경우만
                count += 1  # count 변수에 추가

print(count)
