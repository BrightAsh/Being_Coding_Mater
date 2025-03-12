from collections import deque

def bfs_search(dic,banned_id):
    n = len(banned_id)
    q = deque([[v] for v in dic[banned_id[0]]])
    result = set()
    while q:
        used = q.popleft()
        if len(used) ==n:
            result.add(tuple(sorted(used)))
            continue

        for v in dic[banned_id[len(used)]]:
            if v not in used:
                q.append(used + [v])
    return len(result)
        
def solution(user_id, banned_id):
    dic = {i:[] for i in banned_id}
    for u in user_id:
        for b in banned_id:
            flag=0
            if len(u)==len(b):
                for i in range(len(u)):
                    if b[i]!='*' and b[i]!=u[i]:
                        flag=0
                        break   
                    flag=1
            if flag and u not in dic[b]:
                dic[b].append(u)
    return bfs_search(dic, banned_id)