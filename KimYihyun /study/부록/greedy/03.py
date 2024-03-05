# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

S = input()

def change_str(S):
    cnt = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            cnt += 1 # 다를 경우마다 카운팅
    return (cnt + 1) // 2 # 최소 횟수를 계산


print(change_str(S))
