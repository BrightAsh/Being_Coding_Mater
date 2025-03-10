from collections import deque

def solution(n, computers):
    result = 0 
    answer=[]
    
    for i in range(n):
        if i not in answer:
            q=deque()
            q.append((computers[i],i))
            while q:
                relation,idx=q.popleft()
                for j,r in enumerate(relation):
                    if j != idx and r ==1 and j not in answer:
                        q.append((computers[j],j))
                        answer.append(j)
            result+=1
    
    return result