from collections import defaultdict, deque

def solution(board):
    answer = 0
    n = len(board)
    x1, y1 = 0, 0
    x2, y2 = 0, 1
    
    def in_range(x1, y1, x2, y2):
        return 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n
    
    def in_range1(x, y):
        return 0 <= x < n and 0 <= y < n
    
    visited = defaultdict(int)
    
    # 상우하좌 (시계방향 회전)
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
        
    def bfs():
        q = deque()
        visited[(x1, y1, x2, y2)] = 0
        q.append((x1, y1, x2, y2, 0, 0))
        ans = 0
        
        while q:
            curx1, cury1, curx2, cury2, cur_r, cur_t = q.popleft()
            
            if curx2 == n - 1 and cury2 == n - 1:
                return cur_t
            
            
            # move
            for dx, dy in zip(dxs, dys):
                nx1, ny1, nx2, ny2 = curx1 + dx, cury1 + dy, curx2 + dx, cury2 + dy
                
                if not in_range(nx1, ny1, nx2, ny2):
                    continue
                if board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
                    continue
                if (nx1, ny1, nx2, ny2) not in visited or visited[(nx1, ny1, nx2, ny2)] > cur_t + 1:
                    visited[(nx1, ny1, nx2, ny2)] = cur_t + 1
                    q.append((nx1, ny1, nx2, ny2, cur_r, cur_t + 1))
                    
            # rotate
            points = []
            if cur_r == 0:
                points = [
                    [curx1-1, cury1, curx1, cury1, curx2-1, cury2], 
                    [curx1, cury1, curx1+1, cury1, curx2+1, cury2],
                    [curx2-1, cury2, curx2, cury2, curx1-1, cury1],
                    [curx2, cury2, curx2+1, cury2, curx1+1, cury1]     
                ]
            elif cur_r == 1:
                points = [
                    [curx1, cury1-1, curx1, cury1, curx2, cury2-1],
                    [curx1, cury1, curx1, cury1+1, curx2, cury2+1],
                    [curx2, cury2-1, curx2, cury2, curx1, cury1-1],
                    [curx2, cury2, curx2, cury2+1, curx1, cury1+1]
                ]
                
            for nx1, ny1, nx2, ny2, chx, chy in points:
                if not in_range(nx1, ny1, nx2, ny2):
                    continue
                if board[nx1][ny1] == 1 or board[nx2][ny2] == 1 or board[chx][chy] == 1:
                    continue
                if (nx1, ny1, nx2, ny2) not in visited or visited[(nx1, ny1, nx2, ny2)] > cur_t + 1:
                    visited[(nx1, ny1, nx2, ny2)] = cur_t + 1
                    
                    if cur_r == 0:
                        q.append((nx1, ny1, nx2, ny2, 1 , cur_t + 1))
                    else:
                        q.append((nx1, ny1, nx2, ny2, 0 , cur_t + 1))
                    
            
                    
    answer = bfs()
    return answer