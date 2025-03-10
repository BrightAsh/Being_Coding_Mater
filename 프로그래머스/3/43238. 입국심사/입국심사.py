def solution(n, times):
    s, e = 1, max(times)*n
    
    
    answer = e
    
    while s<=e:
        mid=(s+e)//2
        
        t=sum(mid//time for time in times)
        
        if t>=n:
            answer=mid
            e=mid-1
        else:
            s=mid+1
            
    return answer