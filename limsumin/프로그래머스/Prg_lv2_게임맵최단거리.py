# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    # 행, 열
    n = len(maps)
    m = len(maps[0])
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    visited = [[0] * m for _ in range(n)]
    
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y, 1))
        visited[x][y] = 1
        
        while q:
            cur_x, cur_y, dist = q.popleft()
            
            for i in range(4):
                nx, ny = cur_x + dxs[i], cur_y + dys[i]
                
                if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 1:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = dist + 1
        
        
        return visited[n-1][m-1]
    
    res = bfs(0, 0)
    
    return -1 if res == 0 else res