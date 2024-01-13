# 윷놀이
# https://www.acmicpc.net/problem/2490

res = ''

for i in range(3):
    sticks = list(map(int, input().split()))
    front = 0 # 배의 개수
    back = 0 # 등의 개수
    for j in range(4):
        # 4번 돌면서 0과 1의 각 개수를 센다
        if sticks[j] == 0:
            front += 1
        elif sticks[j] ==1:
             back += 1
    # 총 4개 밖에 없으므로, front/back 중에 하나를 이용해서 검사해도 됨
    if front == 0:
        print('E')
    elif front == 1:
        print('A')
    elif front == 2:
        print('B')
    elif front == 3:
        print('C')
    elif front == 4:
        print('D')
