n,k = map(int,input().split())
l = [i for i in range(1,n+1) if n%i==0]
print(l[k-1] if k <= len(l) else 0)