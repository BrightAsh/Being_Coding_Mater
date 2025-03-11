tmp = float('-inf')
people = 0
for _ in range(10):
    m,p = map(int,input().split())
    people = people-m+p
    if people > tmp:
        tmp = people
print(tmp)