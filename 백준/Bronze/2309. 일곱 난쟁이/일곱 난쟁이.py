import itertools as it
l = [int(input()) for _ in range(9)]
for s in it.combinations(l,7):
    if sum(s) == 100:
        for x in sorted(s):
            print(x)
        exit()