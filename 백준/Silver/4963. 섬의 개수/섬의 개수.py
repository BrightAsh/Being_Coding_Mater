import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
w, h = map(int,input().split())
result = []
def dfs(x,y):
    v[x][y] = True
    for dx,dy in [(-1,-1),(-1,0),(-1,1),(1,1),(1,0),(1,-1),(0,-1),(0,1)]:
        nx, ny = x+dx,y+dy
        if 0 <= nx < h and 0 <= ny < w and not v[nx][ny] and g[nx][ny] == 1:
            dfs(nx,ny)
while w!=0 and h!=0:
    g = []
    v = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0
    for _ in range(h):
        g.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if g[i][j] !=0 and not v[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt)
    w, h = map(int,input().split())

