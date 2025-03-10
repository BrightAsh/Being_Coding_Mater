def solution(routes):
    r = sorted(routes, key = lambda x: (x[1]))
    
    cnt=1
    a=r[0][1]
    print(r)
    for idx in range(1,len(routes)):
        if a<r[idx][0]:
            a=r[idx][1]
            cnt+=1
    return cnt