# 미로 탈출 5-11.py
# 틀림

N, M = map(int, input().split())
maze = []
count = 1

for i in range(N):
    maze.append(list(map(int, input())))  # 맵 정보 입력받기


def exit(x, y):
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    if maze[x][y] == 1:
        # exit(x-1, y)
        exit(x+1, y)
        exit(x, y-1)
        # exit(x, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if exit(i, j) == True:
            count += 1
print(count)
