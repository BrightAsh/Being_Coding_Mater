from collections import deque

def solution(maps):
    n,m =len(maps),len(maps[0])
    v = [[False]*m for _ in range(n)]
    q = deque([(0,0,1)])
    
    while q:
        x,y,cnt = q.popleft()
        
        if x == n-1 and y == m-1:
            return cnt
        
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            
            if 0<=nx<n and 0<=ny<m and not v[nx][ny] and maps[nx][ny]==1:
                v[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return -1