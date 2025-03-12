n=int(input())
if n == 0:
    print(0)
elif n ==1:
    print(1)
else:
    l=[0,1]
    for _ in range(n-1):
        l.append(l[-1]+l[-2])
    print(l[-1])