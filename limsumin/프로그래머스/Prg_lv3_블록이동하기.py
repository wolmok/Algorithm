from collections import defaultdict, deque

def solution(board):
    answer = 0
    n = len(board)
    x1, y1 = 0, 0
    x2, y2 = 0, 1
    
    def in_range(x1, y1, x2, y2):
        return 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n
    
    visited = defaultdict(bool)
    
    # 상하좌우
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    def bfs():
        q = deque()
        visited[(x1, y1, x2, y2)] = True
        q.append((x1, y1, x2, y2, 0))
        ans = 0
        
        while q:
            curx1, cury1, curx2, cury2, cur_t = q.popleft()
            
            for dx, dy in zip(dxs, dys):
                nx1, ny1, nx2, ny2 = curx1 + dx, cury1 + dy, curx2 + dx, cury2 + dy
                
                if in_range(nx1, ny1, nx2, ny2) and board[nx1][ny1] != 1 and board[nx2][ny2] != 1 and (nx1, ny1, nx2, ny2) not in visited:
                    visited[(nx1, ny1, nx2, ny2)] = True
                    q.append((nx1, ny1, nx2, ny2, cur_t + 1))
                    
    bfs()
    return answer