import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    tmp = True
    n = int(input())
    l = sorted([input().strip() for _ in range(n)])
    for i in range(n-1):
        if l[i+1].startswith(l[i]):
            print('NO')
            tmp = False
            break

    if tmp: print('YES') 