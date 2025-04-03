import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline  # 🔥 빠른 입력

n, m = map(int, input().split())
d = {i: [] for i in range(1, n+1)}
v = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

def dfs(k):
    v[k] = True
    for r in d[k]:
        if not v[r]:
            dfs(r)

cnt = 0
for i in range(1, n+1):
    if not v[i]:
        dfs(i)
        cnt += 1

print(cnt)
