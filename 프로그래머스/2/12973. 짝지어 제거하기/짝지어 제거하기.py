def solution(s):
    q= []
    for i in s:
        if q and i == q[-1]: q.pop()
        else: q.append(i)
    return 0 if q else 1