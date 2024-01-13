# 알람 시계
# https://www.acmicpc.net/problem/2884

# 현재 상근이가 설정한 알람 시간
H, M = map(int, input().split())

# 일단 시간, 분을 계산한 후에 시/분 단위로 정확하게 포매팅해주기
# 만약 M이 45 이상일 경우
if (M>=45):
    M -= 45
else:
    # 시간이 0시인 경우
    if (H == 0): 
        H = 23
        M += 15
    # 시간이 0보다 클 경우
    elif (H > 0):
        H -= 1
        M += 15
print(H, M)
