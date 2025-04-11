def solution(routes):
    r = sorted(routes, key = lambda x: (x[1],x[0]))
    cnt=1
    a=r[0][1]
    print(r)
    for s,e in r[1:]:
        if a<s:
            a=e
            cnt+=1
    return cnt