# 음료수 얼려 먹기

import sys

sys.stdin = open("limsumin/study/bfs_dfs/input.txt","rt")

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

result = 0 

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M: # 이동 조건이 아예 안되는 경우
        return
    
    if graph[x][y] == 0: # 얼음인 경우
        graph[x][y] = 1 # 다음에는 탐색하지 않도록 칸막이로 변경
        # 상하좌우 탐색
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: # 얼음인 경우 탐색 시작
            dfs(i, j)
            result += 1
        else:
            continue


print(result)