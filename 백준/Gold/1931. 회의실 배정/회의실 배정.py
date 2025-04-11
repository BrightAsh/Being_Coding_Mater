import sys
input = sys.stdin.readline
n=int(input())
g = sorted([list(map(int,input().split())) for _ in range(n)], key = lambda x: (x[1],x[0]))
cnt = 0
tmp = 0
for s,e in g:
    if tmp <= s:
        cnt+=1
        tmp = e
print(cnt)