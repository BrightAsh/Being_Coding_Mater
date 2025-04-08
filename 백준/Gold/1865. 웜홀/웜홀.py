import sys
input = sys.stdin.readline

def bellman_ford(n,g):
    d = [0] * (n+1)
    
    for i in range(1,n):
        for u,v,w in g:
            if d[v] > d[u]+w:
                d[v] = d[u] +w
    for u,v,w in g:
        if d[v] > d[u]+w:
            return 'YES'
    return 'NO'

tc = int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    g = []
    for _ in range(m):
        s,e,t = map(int,input().split())
        g.append((s,e,t))
        g.append((e,s,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        g.append((s,e,-t))
    print(bellman_ford(n,g))
